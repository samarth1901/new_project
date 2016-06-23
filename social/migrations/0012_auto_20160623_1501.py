# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_auto_20160623_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='expertise',
            field=models.CharField(default=b'Ametuer', max_length=15, choices=[(b'Ametuer', b'Ametuer'), (b'Semi Pro', b'Semi Pro'), (b'Professional', b'Professional'), (b'World Class', b'World Class')]),
        ),
    ]
