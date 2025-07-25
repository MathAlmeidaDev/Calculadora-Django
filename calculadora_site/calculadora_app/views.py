from django.shortcuts import render, redirect
from django.contrib.auth import login, logout # Importa as funções de autenticação
from django.contrib.auth.decorators import login_required # Decorador para proteger as views
from django.contrib.auth.forms import AuthenticationForm # Formulário de autenticação
from django.views.decorators.http import require_POST # Decorador para proteger views de requisições POST
from .models import Operacao # Importa o modelo Operacao
from .forms import CadastroForm # Importa o formulário de cadastro

# Create your views here.


def cadastro_view(request): # Renderiza a página de cadastro
    if request.method == 'POST': # Verifica se o método da requisição é POST
        form = CadastroForm(request.POST) # Cria uma instância do formulário com os dados POST
        if form.is_valid(): # Verifica se o formulário é válido
            user = form.save() # Salva o usuário no banco de dados
            login(request, user) # Faz o login do usuário após o cadastro
            return redirect('calculadora') # Redireciona para a página da calculadora
    else:
        form = CadastroForm() # Cria um formulário vazio para GET

    return render(request, 'core/cadastro.html', {'form': form}) # Renderiza a página de cadastro com o formulário


def login_view(request): # Renderiza a página de login
    if request.method == 'POST': # Verifica se o método da requisição é POST
        form = AuthenticationForm(request, data=request.POST) # Cria uma instância do formulário de autenticação com os dados POST
        if form.is_valid(): # Verifica se o formulário é válido
            user = form.get_user() # Obtém o usuário do formulário
            login(request, user) # Faz o login do usuário
            return redirect('calculadora') # Redireciona para a página da calculadora
        else:
            return render(request, 'core/login.html', {'form': form, 'error': 'Usuário ou senha inválidos.'}) # Se a autenticação falhar, renderiza a página de login com uma mensagem de erro
    else:
        form = AuthenticationForm() # Cria um formulário vazio para GET

    return render(request, 'core/login.html', {'form': form}) # Renderiza a página de login


def logout_view(request): # Função para fazer logout do usuário
    logout(request) # Chama a função de logout
    return redirect('login') # Redireciona para a página de login após o logout


@require_POST # Protege a view para que apenas requisições POST possam acessá-la
@login_required # Protege a view para que apenas usuários autenticados possam acessá-la


def limpar_historico(request):
    Operacao.objects.filter(usuario=request.user).delete() # Deleta todas as operações do usuário autenticado
    return redirect('calculadora') # Redireciona para a página da calculadora após limpar o histórico


def calculadora_view(request):
    historico = Operacao.objects.filter(usuario=request.user).order_by('-dt_inclusao') # Obtém o histórico de operações do usuário autenticado


    if request.method == 'POST': # Verifica se o método da requisição é POST
        expressao = request.POST.get('expressao') # Obtém a expressão da requisição POST
        try:
            resultado = eval(expressao) # Avalia a expressão usando eval
        except Exception:
            resultado = 'Erro' # Se ocorrer um erro, define o resultado como uma mensagem de erro
        Operacao.objects.create(
            usuario=request.user, 
            parametros=expressao, 
            resultado=str(resultado)
        ) # Cria uma nova operação no banco de dados com o usuário, expressão e resultado
        return redirect('calculadora')
    
    return render(request, 'core/calculadora.html', {'historico': historico}) # Renderiza a página da calculadora com o histórico de operações