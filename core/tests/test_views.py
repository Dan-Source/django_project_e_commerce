from django.test import TestCase, Client, override_settings
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model

from model_mommy import mommy

User = get_user_model()
class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy('index')
    
    def tearDown(self):
        pass
    
    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

class ContactViewTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')
    
    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_error(self):
        data = {'name': '', 'message': '', 'email': ''}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')
    
    def test_form_ok(self):
        data = {'name': 'Daniel', 'message': 'test', 'email': 'Meu@email.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do DjangoEcommerce')

class LoginViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = mommy.prepare(User)
        self.user.set_password('123')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()
    
    def test_login_ok(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
