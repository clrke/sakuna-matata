# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('channel', models.ForeignKey(to='api.Channel')),
            ],
        ),
        migrations.AddField(
            model_name='disastermanager',
            name='channel',
            field=models.ForeignKey(default=1, to='api.Channel'),
            preserve_default=False,
        ),
    ]
