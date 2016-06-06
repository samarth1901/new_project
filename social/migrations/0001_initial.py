# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmation_key', models.IntegerField(default=0)),
                ('birthday', models.DateField()),
                ('place', models.CharField(default=b'PUN', max_length=2, choices=[(b'PUN', b'Pune'), (b'BOM', b'Mumbai'), (b'DEL', b'Delhi'), (b'BAN', b'Bangalore'), (b'CHE', b'Chennai')])),
                ('game', models.CharField(default=b'FOT', max_length=10, choices=[(b'FOT', b'Football'), (b'CRI', b'Cricket'), (b'BAS', b'Basketball'), (b'BAD', b'Badminton'), (b'TEN', b'Tennis')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
