# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_project', models.CharField(max_length=100)),
                ('job_function_item', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=1000)),
                ('job_open_time', models.DateTimeField()),
                ('job_goal_time', models.DateTimeField(null=True)),
                ('job_close_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('fox_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='jobs',
            name='job_owner',
            field=models.ForeignKey(to='Version_1.Owners'),
        ),
    ]
