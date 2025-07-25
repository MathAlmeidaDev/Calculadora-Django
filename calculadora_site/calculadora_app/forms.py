from django import forms # Importa o módulo de formulários do Django
from django.contrib.auth.forms import UserCreationForm # Importa o formulário de criação de usuário
from django.contrib.auth.models import User # Importa o modelo de usuário do Django


class CadastroForm(UserCreationForm):
    """
    Formulário para cadastro de novos usuários.
    Herda do UserCreationForm para incluir os campos padrão de criação de usuário.
    """
    email = forms.EmailField(required=True, help_text='Obrigatório. Digite um e-mail válido.')  # Campo adicional para o email do usuário

    class Meta:
        model = User  # Define o modelo associado ao formulário
        fields = ('username', 'email', 'password1', 'password2')  # Campos a serem incluídos no formulário