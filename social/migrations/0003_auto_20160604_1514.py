# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20160604_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
    ]
