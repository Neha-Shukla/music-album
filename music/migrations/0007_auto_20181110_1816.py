# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-10 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20181110_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
