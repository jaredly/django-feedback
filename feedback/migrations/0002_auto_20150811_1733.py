# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='urlhash',
            field=models.TextField(default=b'', null=True, blank=True, verbose_name='urlhash'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='useragent',
            field=models.TextField(default=b'', null=True, blank=True, verbose_name='useragent'),
        ),
    ]
