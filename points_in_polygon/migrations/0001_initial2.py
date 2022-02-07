# Generated by Django 4.0.2 on 2022-02-05 12:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointsInPolygon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('name', models.CharField(max_length=30)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326)),
            ],
        ),
    ]