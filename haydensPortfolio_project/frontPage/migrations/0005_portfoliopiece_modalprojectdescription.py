# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontPage', '0004_auto_20150706_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopiece',
            name='modalProjectDescription',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
    ]
