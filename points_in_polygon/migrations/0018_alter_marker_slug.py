# Generated by Django 4.0.2 on 2022-02-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0017_rename_name_1_ostaniran_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='slug',
            field=models.SlugField(),
        ),
    ]