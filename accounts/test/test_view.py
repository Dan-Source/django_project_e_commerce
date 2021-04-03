from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy
from accounts.models import User
from model_mommy import mommy



class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse_lazy('accounts:register')

    def test_status_code(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_register_ok(self):
        data ={
            'username': 'admin',
            'name': 'Fake Name For User',
            'email': 'mail@mail.com',
            'password1': 'Test#123', 
            'password2': 'Test#123'}
        response = self.client.post(self.register_url, data)
        index_accounts_url = reverse_lazy('index')
        self.assertRedirects(response, index_accounts_url)
        self.assertEquals(User.objects.count(), 1)

    def test_register_error(self):
        data = {'username': 'admin', 'password1': '8520', 'password2': '8520'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(
            response, 'form', 'email', 'Este campo é obrigatório.'
        )

class LoginViewTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.user = mommy.prepare(User)
        self.user.set_password('123')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()
    
    def test_status_code(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)

    def test_login_ok(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_error(self):
        data = {'username': self.user.username, 'password': '123456'}
        response = self.client.post(self.login_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        error_msg = (
        'Por favor, entre com um Apelido/Usuário  e senha corretos. Note que ambos os campos diferenciam maiúsculas e minúsculas.'
        )
        self.assertFormError(response, 'form', None, error_msg)
