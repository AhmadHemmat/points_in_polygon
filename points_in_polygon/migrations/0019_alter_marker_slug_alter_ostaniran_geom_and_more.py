# Generated by Django 4.0.2 on 2022-02-08 16:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0018_alter_marker_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='ostaniran',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
        migrations.AlterField(
            model_name='ostaniran',
            name='name',
            field=models.CharField(max_length=750),
        ),
    ]