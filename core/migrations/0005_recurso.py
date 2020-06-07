# Generated by Django 3.0.7 on 2020-06-07 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200606_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('alterado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('recurso', models.CharField(max_length=50, verbose_name='Recursos')),
                ('bio', models.CharField(max_length=100, verbose_name='Bio')),
                ('icone', models.CharField(choices=[('lni-rocket', 'fogueta'), ('lni-laptop-phone', 'laptop'), ('lni-cog', 'engrenagem'), ('lni-leaf', 'folha'), ('lni-layers', 'camadas'), ('lni-leaf', 'folha2')], max_length=20, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
    ]