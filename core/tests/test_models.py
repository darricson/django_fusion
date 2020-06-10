import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path  # importamos o metodo que queremos testar


class GetFilePathTestCase(TestCase):  # importamos a unidade de codigo que iremos testar, criando dela uma classe

    def setUp(self):
        # criamos um arquivo para fazer comparação.
        # esse arquivo cria a mesma estrutura que queremos comparar o nosso teste, e ficara disponivel para nos.
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        # aqui criamos um novo arquivo chamado
        # 'arquivo' atraves do metodo test_get_file_path
        arquivo = get_file_path(None, 'test.png')
        # e aqui fazemos a comparação se os dois arquivos possuem o mesmo tamanha
        self.assertTrue(len(arquivo), len(self.filename))

# Apos realizarmos o script do teste acima, executamos o comando $ coverage run manage.py test para realizar o teste e
# depois
# Logo apos, executamos o comando $ coverage html, acessamos o diretorio criado htmlcov/, executamos o servidor python
# para verificar a unidade testada e o que mas falta a ser testado $ python -m http.server.
# lembrando que sempre temos de apagar o diretorio gerado do test o *htmlcov


class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)


class EquipeTestCase(TestCase):

    def setUp(self):
        self.equipe = mommy.make('Equipe')

    def test_str(self):
        self.assertEqual(str(self.equipe), self.equipe.nome)


class RecursoTestCase(TestCase):

    def setUp(self):
        self.recurso = mommy.make('Recurso')

    def test_str(self):
        self.assertEqual(str(self.recurso), self.recurso.recurso)


class PrecoTestCase(TestCase):

    def setUp(self):
        self.preco = mommy.make('Preco')

    def test_str(self):
        self.assertEqual(str(self.preco), self.preco.plano)


