# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=50)),
                ('sitter_image', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=1500)),
                ('owner_image', models.CharField(max_length=50)),
                ('dogs', models.CharField(max_length=50)),
                ('sitter', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=50)),
            ],
        ),
    ]