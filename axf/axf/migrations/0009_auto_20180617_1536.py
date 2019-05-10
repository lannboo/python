# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0008_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userAccount', models.CharField(max_length=20)),
                ('productid', models.CharField(max_length=10)),
                ('productnum', models.IntegerField()),
                ('productprice', models.CharField(max_length=10)),
                ('isChose', models.BooleanField(default=True)),
                ('productimg', models.CharField(max_length=150)),
                ('productname', models.CharField(max_length=100)),
                ('orderid', models.CharField(default=b'0', max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CartManaage1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartManaage2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
