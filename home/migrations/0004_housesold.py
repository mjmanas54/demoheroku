# Generated by Django 4.1.1 on 2022-11-11 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_customer_id_customer_customer_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housesold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_deal', models.DateField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('house_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.house')),
            ],
        ),
    ]
