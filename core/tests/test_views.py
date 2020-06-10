from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'jose erick',
            'email': 'jose@gmail.com',
            'assunto': 'assunto quaquer',
            'mensagem': 'mensagem qulquer'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invlaid(self):

        dados = {
            'nome': 'jose erick',
            'email': 'jose@gmail.com'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)

