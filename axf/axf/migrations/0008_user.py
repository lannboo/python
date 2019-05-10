# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0007_foodtype_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userAccount', models.CharField(unique=True, max_length=20)),
                ('userPasswd', models.CharField(max_length=20)),
                ('userName', models.CharField(max_length=20)),
                ('userPhone', models.CharField(max_length=20)),
                ('userAddress', models.CharField(max_length=100)),
                ('userImg', models.CharField(max_length=150)),
                ('userRank', models.IntegerField()),
                ('userToken', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
