from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages  # importando as mensagem de erro ou sucesso

from .models import Servico, Equipe, Recurso, Preco
from .forms import ContatoForm  # faz o import dos forms
# Create your views here.


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm  # importa a class do FormView classe do formulario
    success_url = reverse_lazy('index')  # redireciona para a pagina com sucesso depois que for submetida

    def get_context_data(self, **kwargs):  # metodo que pega os dados do banco
        context = super(IndexView, self).get_context_data(**kwargs)  # joga os dados do banco em um contexto
        context['servicos'] = Servico.objects.order_by('?').all()  # coloca all os atributos de kda model em um contexto
        context['funcionarios'] = Equipe.objects.order_by('?').all()  # order_by('?') deixa os valores aleatorios
        context['recursos'] = Recurso.objects.order_by('?').all()
        context['precos'] = Preco.objects.all()
        return context  # e retorna o contexto de volta para a view

    # se o formulario for valido ele faz isso:
    def form_valid(self, form, *args, **kwargs):  # em cbv temos 2 metodos: um que valida se o form é valido e invalido
        form.send_mail()  # foi chamado o metodo do form criado em ContatoForme para enviar o email
        messages.success(self.request, 'E-mail enviado com sucesso')  # email valido; retorna mensagem de sucesso
        return super(IndexView, self).form_valid(form, *args, **kwargs)  # reton para a view index

    # se o formulario for invalido ele faz isso;
    def form_invalid(self, form, *args, **kwargs):  # metodo de validação de formulario invalido
        messages.error(self.request, 'Erro ao enviar o e-mail')  # mensagem de erro apresentada
        return super(IndexView, self).form_invalid(form, *args, **kwargs)  # retorna para a view index
    # para que o serviço de envio de e-mail funcione, é preciso realizar as configurações do sttings.
