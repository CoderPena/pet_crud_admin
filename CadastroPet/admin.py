import os
from django.contrib import admin
from django.utils import timezone

from django.utils.safestring import mark_safe
from urllib.parse import urlencode

# Register your models here.
from CadastroPet.models import Raca, Pet, Vacinacao, Funcionario

# Importe os modelos que deseja registrar aqui
admin.site.site_title = 'Amigos de São Francisco'
admin.site.site_header = 'Amigos de São Francisco'
admin.site.index_title = 'Administração do Amigos de São Francisco'

#Modo simples
#admin.site.register(Raca)

#Modo decorador (customizavel)
#admin.site.register(Raca)
@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ("raca_id","nome","nivel_cuidado")
    list_display_links = ("raca_id","nome","nivel_cuidado")

    list_filter = ("nivel_cuidado",)
    search_fields = ("nome",)

#admin.site.register(Pet)
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["pet_id","nome","raca_id","data_nascimento", "idade",]
    list_display_links = ("pet_id","nome","raca_id","data_nascimento","idade")

    list_filter = ("raca_id",)
    search_fields = ("nome",)

    def idade(self, obj):
        # Calcula a idade com base na data de nascimento
        idade = (timezone.now().date() - obj.data_nascimento).days // 365
        return idade
    idade.short_description = 'Idade'

    readonly_fields = ["foto_image",]
    def foto_image(self, obj):
        if obj.foto and os.path.isfile(obj.foto.path):
            # Image file exists, proceed with URL generation
            encoded_url = urlencode({'url': obj.foto.url})
            return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
                url=f'/{encoded_url}',  # Add "/" prefix and encoded URL
                width=obj.foto.width,
                height=obj.foto.height,
            ))
        else:
            # Image file doesn't exist, handle appropriately
            return mark_safe('<span class="error">Foto não disponível</span>')


admin.site.register(Vacinacao)

#admin.site.register(Funcionario)
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ["funcionario_id","nome_funcionario","cargo_funcionario","usuario_funcionario",]
    list_display_links = ("funcionario_id","nome_funcionario","cargo_funcionario","usuario_funcionario",)

    list_filter = ("funcionario_id", "nome_funcionario",)
    search_fields = ("funcionario_id", "nome_funcionario", )
