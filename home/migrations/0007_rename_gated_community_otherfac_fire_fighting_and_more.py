# Generated by Django 4.1.1 on 2022-11-11 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_not_sold_house_sold'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otherfac',
            old_name='gated_community',
            new_name='fire_fighting',
        ),
        migrations.RenameField(
            model_name='otherfac',
            old_name='multipurpose_room',
            new_name='temple',
        ),
        migrations.RemoveField(
            model_name='otherfac',
            name='rain_water_harvesting',
        ),
    ]
