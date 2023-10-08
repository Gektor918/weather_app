# Generated by Django 4.2.6 on 2023-10-07 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wind_speed', models.CharField(max_length=50)),
                ('atmosphere_pressure', models.CharField(max_length=50)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
