# Generated by Django 4.0.2 on 2022-02-10 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0028_remove_marker_polygon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marker',
            old_name='polygono',
            new_name='polygon',
        ),
        migrations.RemoveField(
            model_name='ostaniran',
            name='markers',
        ),
    ]
