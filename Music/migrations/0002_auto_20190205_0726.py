# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-05 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
