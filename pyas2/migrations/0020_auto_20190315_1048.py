# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-03-15 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyas2', '0019_auto_20180127_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mdn',
            name='message_id',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='adv_status',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payload',
            name='file',
            field=models.TextField(),
        ),
    ]
