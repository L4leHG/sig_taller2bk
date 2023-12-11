# Generated by Django 3.1.7 on 2023-11-29 14:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Construcciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npn', models.CharField(max_length=30)),
                ('numero_predial', models.CharField(max_length=20, null=True)),
                ('tipo_construccion', models.TextField(null=True)),
                ('area_digitada', models.FloatField(null=True)),
                ('area_cartografica', models.FloatField(null=True)),
                ('comienzo_vida_util', models.DateField(null=True)),
                ('fin_vida_util', models.DateField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npn', models.CharField(max_length=30)),
                ('numero_predial', models.CharField(max_length=20, null=True)),
                ('destino', models.TextField(null=True)),
                ('orip', models.CharField(max_length=3, null=True)),
                ('matricula', models.TextField(null=True)),
                ('area_terreno_digitada', models.FloatField(null=True)),
                ('area_construida_digitada', models.FloatField(null=True)),
                ('area_cartografica', models.FloatField(null=True)),
                ('municipio', models.TextField(null=True)),
                ('departamento', models.TextField(null=True)),
                ('estado', models.IntegerField(null=True)),
                ('direccion', models.TextField(null=True)),
                ('vigencia', models.IntegerField(null=True)),
                ('comienzo_vida_util', models.DateField(null=True)),
                ('fin_vida_util', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terreno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npn', models.CharField(max_length=30)),
                ('numero_predial', models.CharField(max_length=20, null=True)),
                ('area_digitada', models.FloatField(null=True)),
                ('area_cartografica', models.FloatField(null=True)),
                ('comienzo_vida_util', models.DateField(null=True)),
                ('fin_vida_util', models.DateField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npn', models.CharField(max_length=30)),
                ('numero_predial', models.CharField(max_length=40, null=True)),
                ('identificador', models.TextField(null=True)),
                ('planta_ubicacion', models.IntegerField(null=True)),
                ('total_habitaciones', models.IntegerField(null=True)),
                ('total_banios', models.IntegerField(null=True)),
                ('total_locales', models.IntegerField(null=True)),
                ('total_pisos', models.IntegerField(null=True)),
                ('anio_construccion', models.IntegerField(null=True)),
                ('avaluo', models.FloatField(null=True)),
                ('area_construida', models.FloatField(null=True)),
                ('area_cartografica', models.FloatField(null=True)),
                ('uso', models.TextField(null=True)),
                ('comienzo_vida_util', models.DateField(null=True)),
                ('fin_vida_util', models.DateField(null=True)),
                ('construccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.construcciones')),
            ],
        ),
        migrations.CreateModel(
            name='Terreno_Zonas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npn', models.CharField(max_length=30)),
                ('numero_predial', models.CharField(max_length=20, null=True)),
                ('area_digitada', models.FloatField(null=True)),
                ('area_cartografica', models.FloatField(null=True)),
                ('zhf', models.IntegerField(null=True)),
                ('zhg', models.IntegerField(null=True)),
                ('comienzo_vida_util', models.DateField(null=True)),
                ('fin_vida_util', models.DateField(null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('terreno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.terreno')),
            ],
        ),
        migrations.CreateModel(
            name='Alfa_Carto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npn', models.CharField(max_length=30, null=True)),
                ('numero_predial', models.CharField(max_length=20, null=True)),
                ('comienzo_vida_util', models.DateField(null=True)),
                ('fin_vida_util', models.DateField(null=True)),
                ('predio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.predio')),
                ('terreno_zonas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.terreno_zonas')),
                ('unidades_construccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.unidades')),
            ],
        ),
    ]