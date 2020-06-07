# Generated by Django 3.0.7 on 2020-06-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('alterado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('plano', models.CharField(max_length=50, verbose_name='Plano')),
                ('qtd_user', models.CharField(max_length=50, verbose_name='Quantidade de usuarios')),
                ('storage', models.CharField(max_length=50, verbose_name='Armazenamento')),
                ('email', models.CharField(max_length=50, verbose_name='Quantidade de e-mails')),
                ('periodo', models.CharField(max_length=100, verbose_name='Periodo do plano')),
                ('icone', models.CharField(choices=[('lni-package', 'box'), ('lni-drop', 'pingo'), ('lni-star', 'star')], max_length=14, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Preço',
                'verbose_name_plural': 'Preços',
            },
        ),
    ]
