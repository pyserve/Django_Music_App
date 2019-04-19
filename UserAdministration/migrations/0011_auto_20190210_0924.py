# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-10 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAdministration', '0010_userphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_num',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]