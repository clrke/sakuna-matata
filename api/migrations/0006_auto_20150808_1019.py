# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150808_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='message',
            name='mobile_number',
            field=models.CharField(default='09123212321', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='sentiment',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
