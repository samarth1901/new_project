# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_auto_20160610_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='ground',
            name='dp',
            field=models.ImageField(null=True, upload_to=b'ground_pics/', blank=True),
        ),
    ]
