# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.AddField(
            model_name='post',
            name='project_url',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='sourceCode_url',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
