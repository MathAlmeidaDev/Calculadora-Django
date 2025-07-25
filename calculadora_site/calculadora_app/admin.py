from django.contrib import admin
from .models import Operacao

@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin): # Classe para personalizar a exibição do modelo Operacao no admin
    list_display = ('usuario', 'parametros', 'resultado', 'dt_inclusao')
    list_filter = ('usuario',)
    search_fields = ('parametros', 'resultado')