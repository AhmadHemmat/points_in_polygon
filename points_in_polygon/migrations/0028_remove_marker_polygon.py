# Generated by Django 4.0.2 on 2022-02-10 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0027_marker_polygono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marker',
            name='polygon',
        ),
    ]
