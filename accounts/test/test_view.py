from django.test import Client, TestCase
from django.urls import reverse


class InicialTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')
        self.index_url = reverse('accounts:register')

    def test_status_code(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response.status_code, 'index.html')

    # def test_register_ok(self):
    #     data = {'username': 'admin', 'password1': '8520', 'password2': '8520'}
    #     response = self.client.post(self.register_url, data)
    #     self.assertFormError(
    #         response, 'form', 'email', 'Este campo é obrigatório. '
    #     )
    
