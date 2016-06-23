# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_auto_20160621_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ground',
            name='place',
            field=models.CharField(default=b'PUN', max_length=3, choices=[(b'PUN', b'Pune'), (b'BOM', b'Mumbai'), (b'DEL', b'Delhi'), (b'BAN', b'Bangalore'), (b'CHE', b'Chennai')]),
        ),
        migrations.AlterField(
            model_name='team',
            name='game',
            field=models.ForeignKey(to='social.Game'),
        ),
    ]
