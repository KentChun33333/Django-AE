# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Version_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'files/%Y/%m/%d')),
            ],
        ),
    ]
