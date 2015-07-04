# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliopiece',
            name='imagePath',
        ),
        migrations.AddField(
            model_name='portfoliopiece',
            name='image',
            field=models.ImageField(upload_to=b'photos', null=True, verbose_name=b'My Photo'),
            preserve_default=True,
        ),
    ]
