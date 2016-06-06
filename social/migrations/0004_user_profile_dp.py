# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20160604_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='dp',
            field=models.ImageField(null=True, upload_to=b'pic_folder/%self.username', blank=True),
        ),
    ]
