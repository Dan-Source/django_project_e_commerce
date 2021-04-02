from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContatcForm(forms.Form):
    '''
    Formulário para enviar mensagem para contado
    a partir do sistema para a administrador
    '''
    name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {0}\n E-mal: {1}\n {2}'.format(name, email, message)
        send_mail(
            'Contato do DjangoEcommerce', 
            message, 
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )
