# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_owner_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='ground',
            name='place',
            field=models.CharField(default=b'PUN', max_length=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='place',
            field=models.CharField(default=b'PUN', max_length=3, choices=[(b'PUN', b'Pune'), (b'BOM', b'Mumbai'), (b'DEL', b'Delhi'), (b'BAN', b'Bangalore'), (b'CHE', b'Chennai')]),
        ),
    ]
