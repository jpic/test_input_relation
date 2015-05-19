# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20150519_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='name2',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='name3',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
