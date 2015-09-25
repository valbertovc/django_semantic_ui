# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150922_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='attachment',
        ),
    ]
