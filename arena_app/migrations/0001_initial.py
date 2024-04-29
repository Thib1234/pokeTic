# Generated by Django 5.0.4 on 2024-04-29 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Arene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('badge', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='arena_app.badge')),
            ],
        ),
    ]
