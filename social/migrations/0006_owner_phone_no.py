# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20160606_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='phone_no',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
