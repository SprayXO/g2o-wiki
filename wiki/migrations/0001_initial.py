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
            name='Func',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.TextField()),
                ('modifiedtime', models.IntegerField()),
                ('title', models.CharField(max_length=40)),
                ('byedited', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
