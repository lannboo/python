# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0009_auto_20180617_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='productname',
            field=models.CharField(max_length=200),
        ),
    ]
