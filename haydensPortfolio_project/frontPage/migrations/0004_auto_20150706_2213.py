# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontPage', '0003_auto_20150703_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopiece',
            name='modalDescription',
            field=models.CharField(default=b'', max_length=1028),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='portfoliopiece',
            name='modalImage',
            field=models.ImageField(upload_to=b'static/img/haydensPortfolioPieceModals', null=True, verbose_name=b'Modal photo'),
            preserve_default=True,
        ),
    ]
