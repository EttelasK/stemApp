# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detention', '0003_auto_20170420_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='detention',
            name='demerit',
            field=models.ManyToManyField(to='detention.Demerit'),
        ),
    ]
