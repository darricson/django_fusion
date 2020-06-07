from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):

    nome = forms.CharField(label='Nome', max_length=50)
    email = forms.EmailField(label='E-mail', max_length=80)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,  # assunto do e-mail a ser enviado
            body=conteudo,  # conteudo do e-mail
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br',],  # para uem tem de ser enviado
            headers={'Replay-to': email}  # responde ao e-mail recebido
        )
        mail.send()
