# Generated by Django 4.1.3 on 2022-12-06 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('load_capacity', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='DumpTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('side_number', models.CharField(blank=True, max_length=30, unique=True)),
                ('current_load', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dumptruck', to='autoload.truckmodel')),
            ],
        ),
    ]
