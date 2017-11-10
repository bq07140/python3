# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_advertise'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordBrowse',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('browse_goods', models.ForeignKey(to='goods.Goods')),
                ('browse_user', models.ForeignKey(to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
