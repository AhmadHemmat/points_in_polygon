# Generated by Django 4.0.2 on 2022-02-08 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0022_remove_ostaniran_connection_delete_geometry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='polygon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='points_in_polygon.ostaniran'),
        ),
    ]
