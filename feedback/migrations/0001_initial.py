# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('subject', models.CharField(max_length=255, null=True, verbose_name='subject', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email', blank=True)),
                ('text', models.TextField(verbose_name='text')),
                ('site', models.ForeignKey(verbose_name='web', to='sites.Site')),
            ],
        ),
    ]
