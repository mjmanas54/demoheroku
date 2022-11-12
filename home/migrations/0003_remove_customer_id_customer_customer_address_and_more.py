# Generated by Django 4.1.1 on 2022-11-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_city_customer_house_sold_or_not_sold_otherfac_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_address',
            field=models.TextField(default='xyz'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]