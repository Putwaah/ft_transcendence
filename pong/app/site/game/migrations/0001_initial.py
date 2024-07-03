# Generated by Django 5.0.3 on 2024-03-28 12:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.CharField(default='null', max_length=50)),
                ('player2', models.CharField(default='null', max_length=50)),
                ('player1_name', models.CharField(default='null', max_length=50)),
                ('player2_name', models.CharField(default='null', max_length=50)),
                ('modification_game', models.DateTimeField(auto_now=True)),
                ('creation_game', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_user', models.PositiveIntegerField()),
                ('users', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), size=None)),
                ('creation_tournament', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
