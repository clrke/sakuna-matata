# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150808_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='location',
            new_name='description',
        ),
        migrations.AddField(
            model_name='message',
            name='latitude',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='longitude',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
