# Generated by Django 3.1.7 on 2023-12-06 06:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=20, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(null=True, srid=4326)),
            ],
        ),
    ]
