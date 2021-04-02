from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from model_mommy import mommy


User = get_user_model()


class InicialTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse_lazy('accounts:register')
        #self.register_ = reverse('accounts:register')


    def test_status_code(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, 'accounts/register.html')

    # def test_register_ok(self):
    #     data = {'username': 'admin', 'password1': '8520', 'password2': '8520'}
    #     response = self.client.post(self.register_url, data)
    #     self.assertFormError(
    #         response, 'form', 'email', 'Este campo é obrigatório. '
    #     )

class LoginViewTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.user = mommy.prepare(User)
        self.user.set_password('123')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()
    
    def test_login_ok(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    
