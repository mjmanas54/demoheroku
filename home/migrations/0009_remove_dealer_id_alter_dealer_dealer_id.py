# Generated by Django 4.1.1 on 2022-11-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_house_cctv_house_children_play_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='id',
        ),
        migrations.AlterField(
            model_name='dealer',
            name='dealer_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]