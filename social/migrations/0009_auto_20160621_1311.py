# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_ground_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='game',
            field=models.OneToOneField(to='social.Game'),
        ),
        migrations.AlterField(
            model_name='team',
            name='home_ground',
            field=models.OneToOneField(null=True, blank=True, to='social.Ground'),
        ),
    ]
