# Generated by Django 5.0.3 on 2024-05-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroPet', '0007_pet_divulga_pet_texto_divulga'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='data_chegada',
            field=models.DateField(default='2023-05-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='nome_ninhada',
            field=models.CharField(default='N/A', help_text='Digite o nome da ninhada a que pertente.', max_length=100),
        ),
        migrations.AddField(
            model_name='pet',
            name='status_adocao',
            field=models.CharField(choices=[('D', 'Disponível'), ('A', 'Adotado'), ('E', 'Em adaptação'), ('N', 'Não disponível')], default='D', max_length=1),
            preserve_default=False,
        ),
    ]
