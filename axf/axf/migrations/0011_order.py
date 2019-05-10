# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0010_auto_20180617_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderid', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('progress', models.IntegerField()),
            ],
        ),
    ]
