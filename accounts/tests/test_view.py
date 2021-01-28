from django.test import Client, TestCase
from django.urls import reverse


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_ok(self):
        data = {'username': 'admin', 'password1': '8520', 'password2': '8520'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório. ')
    
