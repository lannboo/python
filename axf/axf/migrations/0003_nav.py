# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0002_remove_wheel_isdelete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
        ),
    ]
