# Generated by Django 4.1.1 on 2022-11-11 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=10)),
                ('customer_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='sold_or_not_sold',
            field=models.CharField(default='xyz', max_length=8),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Otherfac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cctv', models.BooleanField()),
                ('children_play_area', models.BooleanField()),
                ('landscape', models.BooleanField()),
                ('multipurpose_room', models.BooleanField()),
                ('garage', models.BooleanField()),
                ('power_backup', models.BooleanField()),
                ('lifts', models.BooleanField()),
                ('cycling_jogging', models.BooleanField()),
                ('gated_community', models.BooleanField()),
                ('rain_water_harvesting', models.BooleanField()),
                ('house_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.house')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('loc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loc_name', models.CharField(max_length=50)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city')),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_id', models.CharField(max_length=10)),
                ('dealer_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('house_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.house')),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city'),
        ),
        migrations.AlterField(
            model_name='house',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.location'),
        ),
    ]
