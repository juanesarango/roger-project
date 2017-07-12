# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sitters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='owner_image',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='sitter_image',
        ),
        migrations.AddField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviews',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='dogs',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='end_date',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitters.Owner'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='sitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitters.Sitter'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='start_date',
            field=models.DateField(max_length=50),
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitters.Owner'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='dogs',
            field=models.ManyToManyField(to='sitters.Dog'),
        ),
    ]