# Generated by Django 4.0.2 on 2022-02-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points_in_polygon', '0007_remove_ostaniran_nl_name_1_alter_ostaniran_cc_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ostaniran',
            name='nl_name_1',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
