from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormeTestCase(TestCase):

    def setUp(self):
        self.nome = 'Gbariel P.'
        self.email = 'gabriel@gmail.com'
        self.assunto = 'Assunto qualquer'
        self.mensagem = 'Mensagem qualquer'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)  # e a mesma coisa de fazer ContatoForm(requist.POST)

    def test_send_mail(self):
        form1 = ContatoForm(self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEqual(res1, res2)
