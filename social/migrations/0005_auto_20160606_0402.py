# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_user_profile_dp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ground',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=60, null=True, blank=True)),
                ('game', models.ForeignKey(to='social.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('place', models.CharField(default=b'PUN', max_length=2, choices=[(b'PUN', b'Pune'), (b'BOM', b'Mumbai'), (b'DEL', b'Delhi'), (b'BAN', b'Bangalore'), (b'CHE', b'Chennai')])),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=10, null=True, blank=True)),
                ('skills', models.CharField(max_length=50, null=True, blank=True)),
                ('game', models.ForeignKey(to='social.Game')),
                ('player', models.ForeignKey(to='social.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('expertise', models.CharField(default=b'AM', max_length=2, choices=[(b'AM', b'Ametuer'), (b'SP', b'Semi Pro'), (b'PR', b'Professional'), (b'WC', b'World Class')])),
                ('game', models.ForeignKey(to='social.Game')),
                ('home_ground', models.ForeignKey(blank=True, to='social.Ground', null=True)),
                ('player', models.ManyToManyField(to='social.Player')),
            ],
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='game',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='place',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='profile_type',
            field=models.CharField(default=b'PL', max_length=2),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='dp',
            field=models.ImageField(null=True, upload_to=b'profile_pics/', blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='user_profile',
            field=models.OneToOneField(to='social.User_profile'),
        ),
        migrations.AddField(
            model_name='owner',
            name='user_profile',
            field=models.OneToOneField(to='social.User_profile'),
        ),
        migrations.AddField(
            model_name='ground',
            name='owner',
            field=models.ForeignKey(to='social.Owner'),
        ),
    ]
