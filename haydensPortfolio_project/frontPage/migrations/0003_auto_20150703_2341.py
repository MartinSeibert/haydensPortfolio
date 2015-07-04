# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontPage', '0002_auto_20150703_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopiece',
            name='image',
            field=models.ImageField(upload_to=b'static/img/haydensPortfolioPieces', null=True, verbose_name=b'My Photo'),
        ),
    ]
