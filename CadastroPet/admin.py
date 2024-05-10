from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe

# Register your models here.
from CadastroPet.models import Raca, Pet, Vacinacao

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
    list_display = ["pet_id","nome","raca_id","data_nascimento", "idade"]
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
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
    )    
#    foto_image = models.ImageField(upload_to='fotos_pet/', blank=True, null=True, verbose_name='Foto do crachá')



admin.site.register(Vacinacao)
