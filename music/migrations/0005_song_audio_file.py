# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-10 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_remove_song_is_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, max_length=10, null=True, upload_to=''),
        ),
    ]
