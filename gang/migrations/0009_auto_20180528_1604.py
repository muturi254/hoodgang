# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gang', '0008_auto_20180528_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='post/pic/%Y-%m-%d'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gang.Category'),
        ),
    ]
