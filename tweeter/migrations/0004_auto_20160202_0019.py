# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0003_auto_20160201_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
