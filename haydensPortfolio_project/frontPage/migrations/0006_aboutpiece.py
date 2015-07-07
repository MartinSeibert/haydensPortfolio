# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontPage', '0005_portfoliopiece_modalprojectdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPiece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/img/aboutPieces', null=True, verbose_name=b'About photo')),
                ('dateHeading', models.CharField(max_length=128)),
                ('descriptionSubheader', models.CharField(default=b'', max_length=256)),
                ('bodyText', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
