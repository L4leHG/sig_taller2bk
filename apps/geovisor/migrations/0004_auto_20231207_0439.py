# Generated by Django 3.1.7 on 2023-12-07 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0003_auto_20231206_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terreno_zonas',
            name='terreno',
        ),
        migrations.RemoveField(
            model_name='unidades',
            name='construccion',
        ),
        migrations.DeleteModel(
            name='Alfa_Carto',
        ),
        migrations.DeleteModel(
            name='Construcciones',
        ),
        migrations.DeleteModel(
            name='Predio',
        ),
        migrations.DeleteModel(
            name='Terreno',
        ),
        migrations.DeleteModel(
            name='Terreno_Zonas',
        ),
        migrations.DeleteModel(
            name='Unidades',
        ),
    ]