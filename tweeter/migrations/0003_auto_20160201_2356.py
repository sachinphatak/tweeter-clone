# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0002_auto_20160201_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 18, 26, 22, 886302, tzinfo=utc)),
        ),
    ]
