# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='distance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='timing',
            name='time',
            field=models.IntegerField(),
        ),
    ]
