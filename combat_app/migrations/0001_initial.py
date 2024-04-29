# Generated by Django 5.0.4 on 2024-04-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pokemon_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pokemons', models.ManyToManyField(to='pokemon_app.pokemon')),
            ],
        ),
    ]
