# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import shortner.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=220, validators=[shortner.validators.validate_url])),
                ('shortcode', models.CharField(blank=True, max_length=15, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
