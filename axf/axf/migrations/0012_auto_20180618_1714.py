# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0011_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartManaage1',
        ),
        migrations.DeleteModel(
            name='CartManaage2',
        ),
    ]
