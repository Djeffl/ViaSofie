# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=255)),
                ('voornaam', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gebruiker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voornaam', models.CharField(max_length=128)),
                ('naam', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('straatnaam', models.CharField(max_length=128)),
                ('huisnr', models.IntegerField()),
                ('busnr', models.CharField(blank=True, max_length=10)),
                ('telefoonnr', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Handelstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('logText', models.CharField(max_length=255)),
                ('gebruiker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Gebruiker')),
            ],
        ),
        migrations.CreateModel(
            name='Pand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('straatnaam', models.CharField(max_length=128)),
                ('huisnr', models.SmallIntegerField()),
                ('gebruiker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Gebruiker')),
                ('handelstatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Handelstatus')),
            ],
        ),
        migrations.CreateModel(
            name='PandType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pandtype', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Stad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.SmallIntegerField()),
                ('stadsnaam', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagnaam', models.CharField(max_length=128)),
                ('pand', models.ManyToManyField(to='webapp.Pand')),
            ],
        ),
        migrations.CreateModel(
            name='Toegangslevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toegangslevelnaam', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Voortgang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='pand',
            name='pandtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.PandType'),
        ),
        migrations.AddField(
            model_name='pand',
            name='postcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Stad'),
        ),
        migrations.AddField(
            model_name='pand',
            name='voortgang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Voortgang'),
        ),
        migrations.AddField(
            model_name='gebruiker',
            name='postcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Stad'),
        ),
        migrations.AddField(
            model_name='gebruiker',
            name='toegangslevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Toegangslevel'),
        ),
        migrations.AddField(
            model_name='foto',
            name='pand',
            field=models.ManyToManyField(to='webapp.Pand'),
        ),
    ]
