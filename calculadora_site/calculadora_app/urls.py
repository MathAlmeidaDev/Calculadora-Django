from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # URL para a view de login
    path('cadastro/', views.cadastro_view, name='cadastro'),  # URL para a view de cadastro
    path('logout/', views.logout_view, name='logout'),  # URL para a view de logout
    path('calculadora/', views.calculadora_view, name='calculadora'),  # URL para a view da calculadora
    path('limpar-historico/', views.limpar_historico, name='limpar_historico'),  # URL para limpar o histórico de operações
]