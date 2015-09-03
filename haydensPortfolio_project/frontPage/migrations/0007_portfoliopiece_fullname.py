# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontPage', '0006_aboutpiece'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopiece',
            name='fullname',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
