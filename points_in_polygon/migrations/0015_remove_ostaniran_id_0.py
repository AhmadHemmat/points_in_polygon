# Generated by Django 4.0.2 on 2022-02-08 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0014_delete_neighborhoods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ostaniran',
            name='id_0',
        ),
    ]
