from django.db import models
from django import forms
from django.utils import timezone

from django.contrib.auth import get_user_model

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
    
User = get_user_model()
class Funcionario(models.Model):
    funcionario_id = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=100, verbose_name='Nome do Funcionário')
    endereço_funcionario = models.CharField(max_length=200, verbose_name='Endereço do Funcionário')
    cargo_funcionario = models.CharField(max_length=50, verbose_name='Cargo do Funcionário')
    email_funcionario = models.CharField(max_length=50, verbose_name='E-mail do Funcionário')
    telefone_funcionario = models.CharField(max_length=30, verbose_name='Telefone do Funcionário')
    usuario_funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.funcionario_id) + ' | ' + str(self.nome_funcionario)

User = get_user_model()
class Voluntario(models.Model):
    voluntario_id = models.AutoField(primary_key=True)
    nome_voluntario = models.CharField(max_length=100, verbose_name='Nome do Voluntario')
    endereço_voluntario = models.CharField(max_length=200, verbose_name='Endereço do Voluntario')
    atribuicao_voluntario = models.TextField(max_length=5000, verbose_name='Atribuições do Voluntario', help_text='Detalhe aqui as atribuições do voluntário')
    email_voluntario = models.CharField(max_length=50, verbose_name='E-mail do Voluntario')
    telefone_voluntario = models.CharField(max_length=30, verbose_name='Telefone do Voluntario')
    usuario_voluntario = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.voluntario_id) + ' | ' + str(self.nome_voluntario)

User = get_user_model()
class Patrocinador(models.Model):
    OPCOES_PATROCINIO = [
        ('1', 'Financeiro'),
        ('2', 'Serviços Veterinários'),
        ('3', 'Alimentos e Suprimentos'),
        ('4', 'Esterilização/Castração'),
        ('0', 'Outros'),
    ]

    patrocinador_id = models.AutoField(primary_key=True)
    nome_patrocinador = models.CharField(max_length=100, verbose_name='Nome do Patrocinador')
    endereço_patrocinador = models.CharField(max_length=200, verbose_name='Endereço do Patrocinador')
    email_patrocinador = models.CharField(max_length=50, verbose_name='E-mail do Patrocinador')
    telefone_patrocinador = models.CharField(max_length=30, verbose_name='Telefone do Patrocinador')
    usuario_patrocinador = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Usuário de Sistema do Patrocinador')
    tipo_patrocinio = models.CharField(max_length=1, choices=OPCOES_PATROCINIO, verbose_name='Tipo de Patrocínio')
    descricao_patrocinio = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Descrição do Patrocínio', help_text='Detalhe aqui o patrocínio')
    pets_patrocinados = models.ManyToManyField(Pet)

    def __str__(self):
        return str(self.patrocinador_id) + ' | ' + str(self.nome_patrocinador)

User = get_user_model()
class Adotante(models.Model):
    adotante_id = models.AutoField(primary_key=True)
    nome_adotante = models.CharField(max_length=100, verbose_name='Nome do Adontante')
    endereço_adotante = models.CharField(max_length=200, verbose_name='Endereço do Adontante')
    email_adotante = models.CharField(max_length=50, verbose_name='E-mail do Adontante')
    telefone_adotante = models.CharField(max_length=30, verbose_name='Telefone do Adontante')
    usuario_adotante = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Usuário de Sistema do Adontante')
    observacao_adotante = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Observação da Adoção/Adotante', help_text='Detalhe aqui a obsrevação da Adoção/Adontante')
    pets_adotados = models.ManyToManyField(Pet, limit_choices_to={'status_adocao': 'D'})

    def __str__(self):
        return str(self.adotante_id) + ' | ' + str(self.nome_adotante)

User = get_user_model()
class LarTemporario(models.Model):
    lartemporario_id = models.AutoField(primary_key=True)
    descricao_lartemporario = models.CharField(max_length=100, verbose_name='Nome do Lar Temporário')
    responsavel_lartemporario = models.CharField(max_length=100, verbose_name='Nome do responsável pelo Lar Temporário')
    endereço_lartemporario = models.CharField(max_length=200, verbose_name='Endereço do Lar Temporário')
    email_lartemporario = models.CharField(max_length=50, verbose_name='E-mail do Lar Temporário')
    telefone_lartemporario = models.CharField(max_length=30, verbose_name='Telefone do Lar Temporário')
    usuario_alartemporario = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Usuário de Sistema do Lar Temporário')
    observacao_lartemporario = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Observação do Lar Temporário', help_text='Detalhe aqui a observação do Lar Temporário')
    capacidade_laartemporario = models.IntegerField(verbose_name='Capacidade do Lar Temporário')
    pets_lartemporario = models.ManyToManyField(Pet, verbose_name='Selecione os PETs para este Lar Temporário', help_text='Selecione os PETs para este Lar Temporário')

    def __str__(self):
        return str(self.lartemporario_id) + ' | ' + str(self.descricao_lartemporario)

