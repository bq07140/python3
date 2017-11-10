# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_recordbrowse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordbrowse',
            name='browse_goods',
        ),
        migrations.RemoveField(
            model_name='recordbrowse',
            name='browse_user',
        ),
        migrations.DeleteModel(
            name='RecordBrowse',
        ),
    ]
