# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 18, 6, 47, 272692, tzinfo=utc)),
        ),
    ]
