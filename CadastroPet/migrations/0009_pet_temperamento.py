# Generated by Django 5.0.3 on 2024-05-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroPet', '0008_pet_data_chegada_pet_nome_ninhada_pet_status_adocao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='temperamento',
            field=models.CharField(choices=[('N', 'Normal'), ('H', 'Hiperativo'), ('M', 'Medroso'), ('A', 'Agressivo'), ('S', 'Manso'), ('C', 'Sociável com outros animais'), ('O', 'Outros')], default='N', max_length=1),
            preserve_default=False,
        ),
    ]
