from django.contrib import admin
from .models import Cargo, Servico, Equipe, Recurso, Preco

# Register your models here.


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'alterado')


@admin.register(Servico)
class SevicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'alterado')


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'alterado')


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'bio', 'ativo', 'alterado')


@admin.register(Preco)
class PrecoAdmin(admin.ModelAdmin):
    list_display = ('plano', 'preco', 'ativo', 'storage')
