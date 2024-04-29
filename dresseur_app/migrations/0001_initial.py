# Generated by Django 5.0.4 on 2024-04-29 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arena_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PNJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('argent', models.IntegerField()),
                ('phrase_accroche', models.CharField(max_length=255)),
                ('est_champion', models.BooleanField()),
                ('arene', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arena_app.arene')),
            ],
        ),
        migrations.CreateModel(
            name='Ligue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('champion', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dresseur_app.pnj')),
            ],
        ),
    ]
