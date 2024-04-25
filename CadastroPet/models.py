from django.db import models
from django import forms
from django.utils import timezone   

# Create your models here.
# class Raca(models.Model):
#     raca_id = models.AutoField(primary_key=True)
#     nome = models.CharField(max_length=100)
#     nivel_cuidado = models.CharField(max_length=20)
#     caracteristica = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.nome

class Raca(models.Model):
    OPCOES_NIVEL_CUIDADO = [
        ('Alto', 'Alto'),
        ('Medio', 'Médio'),
        ('Baixo', 'Baixo'),
        ('Diversificado', 'Diversificado'),
        ('N/A', 'N/A'),
    ]
    
    raca_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    nivel_cuidado = models.CharField(
        max_length=20,
        choices=OPCOES_NIVEL_CUIDADO,
        default='DIVERSIFICADO',  # Se desejar definir um valor padrão
    )
    caracteristica = models.TextField(max_length=5000, default='N/A')

    def __str__(self):
        return str(self.raca_id) + ' | ' + self.nome
    
class Pet(models.Model):
    OPCOES_PORTE = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]

    pet_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    raca_id = models.ForeignKey(Raca, on_delete=models.SET_NULL, null=True)
    porte = models.CharField(max_length=1, choices=OPCOES_PORTE)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='fotos_pet/', blank=True, null=True)
    historico = models.TextField(max_length=5000, default='N/A')

    def __str__(self):
        return str(self.pet_id) + ' | ' + self.nome
    
class Vacinacao(models.Model):
    vacinacao_id = models.AutoField(primary_key=True)
    pet_id = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    data_vacinacao = models.DateField(default=timezone.now, help_text = "Use o formato: <em>DD-MM-YYYY</em>.")
    descricao = models.TextField(max_length=5000, help_text='Detalhe aqui a vacinação')

    def __str__(self):
        return str(self.vacinacao_id) + ' | ' + str(self.data_vacinacao)