# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171108_1431'),
        ('goods', '0003_recordbrowse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cart_amount', models.IntegerField()),
                ('cart_goods', models.ForeignKey(to='goods.Goods')),
                ('cart_user', models.ForeignKey(to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
