# Generated by Django 4.0.2 on 2022-02-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0012_alter_ostaniran_name_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]