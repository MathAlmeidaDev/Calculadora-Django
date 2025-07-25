from django.db import models
from django.contrib.auth.models import User # Importa o modelo User do Django para associar usuários às operações

class Operacao(models.Model):
    """
    Modelo para armazenar as operações realizadas na calculadora.
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Associa a operação a um usuário
    parametros = models.CharField(max_length=100)  # Campo para armazenar a operação (ex: "2 + 2")
    resultado = models.CharField(max_length=100)  # Campo CharField para armazenar o resultado da operação porque é flexível, aceita números e strings como "Erro".
    dt_inclusao = models.DateTimeField(auto_now_add=True)  # Data e hora da operação

    def __str__(self):
        return f"{self.parametros} = {self.resultado}" 
