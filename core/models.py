import uuid
from django.db import models
from stdimage.models import StdImageField
# Create your models here.


# metodo que pega o arquivo de imagem, separa a extnsa0 e recria com um novo nome
# uuid faz a geração aleatoria do nome do arquivo de imagem
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField(auto_now_add=True, verbose_name='Criado')
    alterado = models.DateField(auto_now=True, verbose_name='Atualizado')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        abstract = True


class Servico(Base):
    SERVICO_CHOICHES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-user', 'Usuarios'),
        ('lni-layers', 'Designer'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField(max_length=100, verbose_name='Serviços')
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    icone = models.CharField(max_length=12, choices=SERVICO_CHOICHES, verbose_name='Icone')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField(max_length=100, verbose_name='Cargo')

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Equipe(Base):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo')
    bio = models.CharField(max_length=200, verbose_name='Biografia')
    imagem = StdImageField(upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480}}, verbose_name='Imagem')
    facebook = models.CharField(max_length=50, verbose_name='Facebook', default='#')
    twiter = models.CharField(max_length=50, verbose_name='Twiter', default='#')
    instagram = models.CharField(max_length=50, verbose_name='Instagram', default='#')

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.nome


class Recurso(Base):

    RECURSOS_CHOICES = (
        ('lni-rocket', 'fogueta'),
        ('lni-laptop-phone', 'laptop'),
        ('lni-cog', 'engrenagem'),
        ('lni-leaf', 'folha'),
        ('lni-layers', 'camadas'),
        ('lni-leaf', 'folha2'),
    )
    recurso = models.CharField(max_length=50, verbose_name='Recursos')
    bio = models.CharField(max_length=100, verbose_name='Bio')
    icone = models.CharField(max_length=20, choices=RECURSOS_CHOICES, verbose_name='Icone')

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso


class Preco(Base):

    PRECOS_CHOICES = (
        ('lni-package', 'box'),
        ('lni-drop', 'pingo'),
        ('lni-star', 'star'),
    )

    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')
    plano = models.CharField(max_length=50, verbose_name='Plano')
    qtd_user = models.CharField(max_length=50, verbose_name='Quantidade de usuarios')
    storage = models.CharField(max_length=50, verbose_name='Armazenamento')
    email = models.CharField(max_length=50, verbose_name='Quantidade de e-mails')
    periodo = models.CharField(max_length=100, verbose_name='Periodo do plano')
    icone = models.CharField(max_length=14, choices=PRECOS_CHOICES, verbose_name='Icone')

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.plano
