# Generated by Django 3.1.2 on 2020-11-03 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videojuegos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pegi', models.CharField(blank=True, choices=[('p3', 'PEGI 3'), ('P7', 'PEGI 7'), ('P12', 'PEGI 12'), ('P16', 'PEGI 16'), ('P18', 'PEGI 18')], default='p3', help_text='Clasificación por edad ', max_length=3)),
            ],
        ),
    ]