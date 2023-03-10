# Generated by Django 4.1.5 on 2023-02-07 22:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Template_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_id', models.IntegerField(default=0)),
                ('event_id', models.IntegerField(default=0)),
                ('name', models.CharField(default='default', max_length=40)),
                ('description', models.CharField(default='default', max_length=200)),
                ('date_start', models.DateField(default=datetime.datetime(2023, 2, 8, 5, 32, 30, 540123))),
                ('date_end', models.DateField(default=datetime.datetime(2023, 2, 8, 5, 32, 30, 540123))),
                ('address', models.CharField(default='default', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_template', models.IntegerField(default=0)),
                ('id_global', models.IntegerField(default=0)),
                ('male_name', models.CharField(default='default', max_length=40)),
                ('female_name', models.CharField(default='default', max_length=40)),
                ('date', models.DateField(default=datetime.datetime(2023, 2, 8, 5, 32, 30, 540123))),
                ('img', models.ImageField(default=None, upload_to='images/')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='members.accountdb')),
            ],
        ),
    ]
