# Generated by Django 4.0.2 on 2022-02-10 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0026_alter_ostaniran_markers'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='polygono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marker', to='points_in_polygon.ostaniran'),
        ),
    ]
