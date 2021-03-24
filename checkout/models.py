#from pagseguro import PagSeguro
import requests
from xml.etree import ElementTree

from django.db import models
from django.conf import settings
from catalog.models import Product

class CartItemManager(models.Manager):
    
    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(
                cart_key=cart_key, product=product, price=product.price
            )
        return cart_item, created

class CartItem(models.Model):
    
    cart_key = models.CharField(
        'Chave do Carrinho', max_length=40, db_index=True
    )
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key', 'product'),)

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)

class OrderManager(models.Manager):
    
    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order, 
                quantity=cart_item.quantity, 
                product=cart_item.product,
                price=cart_item.price
            )
        return order

class Order(models.Model):
    
    STATUS_CHOICES = (
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )

    PAYMENT_OPTION_CHOICES = (
        ('deposit', 'Depósito'),
        ('pagseguro', 'PagSeguro'),
        ('paypal', 'Paypal'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário', 
        on_delete=models.CASCADE
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )
    payment_option = models.CharField(
        'Opção de Pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=20,
        default='deposit'
    )

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)

    def products(self):
        products_ids = self.items.values_list('product')
        return Product.objects.filter(pk__in=products_ids)

    def total(self):
        aggregate_queryset = self.items.aggregate(
            total=models.Sum(
                models.F('price') * models.F('quantity'),
                output_field=models.DecimalField()
            )
        )
        return aggregate_queryset['total']

    def pagseguro_update_status(self, status):
        if status == '3':
            self.status = 1
        elif status == '7':
            self.status = 2
        self.save()

    def complete(self):
        self.status = 1
        self.save()

    def pagseguro(self):
        self.payment_option = 'pagseguro'
        self.save()

        email=settings.PAGSEGURO_EMAIL
        token=settings.PAGSEGURO_TOKEN
        url = 'https://ws.sandbox.pagseguro.uol.com.br/v2/checkout?'+
            'email={{email}}&token={{token}}'
'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        payload ={
            'email': '{{email}}',
            token': '{{token}}',
            'currency': 'BRL',
            'itemId1': '0001',
            'itemDescription1': 'Notebook Prata',
            'itemAmount1': '100.00',
            'itemQuantity1': 1,
            'itemWeight1': 1000,
            'reference': 'REF1234',
            'senderName': 'Jose Comprador',
            'senderAreaCode': 11,
            'senderPhone': 56713293,
            'senderCPF': 38440987803,
            'senderBornDate': '12/03/1990',
            'senderEmail': 'email@sandbox.pagseguro.com.br',
            'shippingType': 1,
            'shippingAddressStreet': 'Av.Brig.Faria Lima',
            'shippingAddressNumber': 1384,
            'shippingAddressComplement': '2o andar',
            'shippingAddressDistrict': 'Jardim Paulistano',
            'shippingAddressPostalCode': '01452002',
            'shippingAddressCity': 'Sao Paulo',
            'shippingAddressState': 'SP',
            'shippingAddressCountry': 'BRA',
            'extraAmount': -0.01,
            'redirectURL': reverse("checkout:order_detail"),
            'notificationURL': 'https://yourserver.com/nas_ecommerce/277be731-3b7c-4dac-8c4e-  4c3f4a1fdc46/',
            'maxUses': 1,
            'maxAge': 3000,
            'shippingCost': '1.00'
        }
        
        sender = self.user.email
        corrency = 'BRL'

        auth = {'email': email, 'token': token}
        pagseguro_items = {}
        for item in self.items.all():
            item = {
                "id": item.product.id,
                "description": item.product.name, 
                "amount": '{:2f}'.format(item.price),
                "quantity": item.quantity

            }
        redirectURL = reverse_lazy('checkout:order_detail')

            
        r = requests.post(
            url,
            data=payload,
            headers=headers
        )
        string_xml = response.content
        xml_tree = ElementTree.fromstring(string_xml)
        return xml_tree

    def paypal(self):
        self.payment_option = 'paypal'
        self.save()
        paypal_dict = {
            'upload': '1',
            'business': settings.PAYPAL_EMAIL,
            'invoice': self.pk,
            'cmd': '_cart',
            'currency_code': 'BRL',
            'charset': 'utf-8',
        }
        index = 1
        for item in self.items.all():
            paypal_dict['amount_{}'.format(index)] = '%.2f' % item.price
            paypal_dict['item_name_{}'.format(index)] = item.product.name
            paypal_dict['quantity_{}'.format(index)] = item.quantity
            index = index + 1
        return paypal_dict


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order, verbose_name='Pedido', 
        related_name='items', 
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        'catalog.Product', 
        verbose_name='Produto', 
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens dos pedidos'

    def __str__(self):
        return '[{}] {}'.format(self.order, self.product)


def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()


models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)
