# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-28 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0007_order_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='product', max_length=255),
            preserve_default=False,
        ),
    ]
