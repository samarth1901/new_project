# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_auto_20160623_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='home_ground',
            field=models.ForeignKey(blank=True, to='social.Ground', null=True),
        ),
    ]
