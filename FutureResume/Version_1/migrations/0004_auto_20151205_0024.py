# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Version_1', '0003_auto_20151204_0435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_project', models.CharField(max_length=100)),
                ('job_function_item', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=1000)),
                ('job_open_time', models.DateTimeField()),
                ('job_goal_time', models.DateTimeField(null=True)),
                ('job_close_time', models.DateTimeField(null=True)),
                ('job_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='job_owner',
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
    ]
