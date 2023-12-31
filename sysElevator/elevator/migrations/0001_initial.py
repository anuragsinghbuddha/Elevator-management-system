# Generated by Django 4.2.4 on 2023-08-26 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operational', models.BooleanField(default=True)),
                ('current_floor', models.IntegerField(default=1)),
                ('moving_up', models.BooleanField(default=True)),
                ('doors_open', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('direction', models.CharField(max_length=4)),
                ('completed', models.BooleanField(default=False)),
                ('elevator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elevator.elevator')),
            ],
        ),
    ]
