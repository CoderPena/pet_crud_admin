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
    OPCOES_ESPECIE = [
        ('C', 'Canina'),
        ('F', 'Felina'),
    ]
    OPCOES_PORTE = [
        ('P', 'Pequeno'),   
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]
    OPCOES_SIM_NAO = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    OPCOES_ADOCAO = [
        ('D', 'Disponível'),
        ('A', 'Adotado'),
        ('E', 'Em adaptação'),
        ('N', 'Não disponível'),
    ]
    OPCOES_TEMPERAMENTO = [
        ('N', 'Normal'),
        ('H', 'Hiperativo'),
        ('M', 'Medroso'),
        ('A', 'Agressivo'),
        ('S', 'Manso'),
        ('C', 'Sociável com outros animais'),
        ('O', 'Outros'),
    ]

    pet_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,verbose_name='Nome do Pet')
    nome_ninhada = models.CharField(blank=True, null=True, max_length=100, default='N/A', verbose_name='Nome da ninhada', help_text="Digite o nome da ninhada a que pertente.")
    especie = models.CharField(max_length=1, choices=OPCOES_ESPECIE, verbose_name='Espécie')
    raca_id = models.ForeignKey(Raca, on_delete=models.SET_NULL, null=True, verbose_name='ID da raça')
    porte = models.CharField(max_length=1, choices=OPCOES_PORTE, verbose_name='Porte do animal')
    data_nascimento = models.DateField(verbose_name='Data do nascimento')
    foto = models.ImageField(upload_to='fotos_pet/', blank=True, null=True, verbose_name='Foto do crachá')
    historico = models.TextField(blank=True, null=True, max_length=5000, default='N/A', verbose_name='Histórico', help_text="Digite os antecedentes do animal e características de personalidade e comportamentais.")
    data_chegada = models.DateField(verbose_name='Data de Chegada na ONG')

    divulga = models.CharField(max_length=1, choices=OPCOES_SIM_NAO, verbose_name='Divulgação', help_text="Permite texto de divulgação externa?")
    texto_divulga = models.TextField(blank=True, null=True, max_length=5000, default='N/A', verbose_name='Texto para divulgação', help_text="Digite o texto para divulgação externa.")
    temperamento = models.CharField(max_length=1, choices=OPCOES_TEMPERAMENTO, verbose_name='Temperamento do animal')
    doencas = models.TextField(blank=True, null=True, max_length=5000, default='N/A', help_text="Digite as doenças do animal.")

    status_adocao = models.CharField(max_length=1, choices=OPCOES_ADOCAO)
    data_obito = models.DateField(blank=True, null=True, verbose_name='Data do óbito')
    motivo_obito = models.CharField(max_length=100, blank=True, null=True, verbose_name='Motivo óbito')

    def __str__(self):
        return str(self.pet_id) + ' | ' + self.nome
    
class Vacinacao(models.Model):
    vacinacao_id = models.AutoField(primary_key=True)
    pet_id = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    data_vacinacao = models.DateField(default=timezone.now, help_text = "Use o formato: <em>DD-MM-YYYY</em>.")
    descricao = models.TextField(max_length=5000, help_text='Detalhe aqui a vacinação')

    def __str__(self):
        return str(self.vacinacao_id) + ' | ' + str(self.data_vacinacao)