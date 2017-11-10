# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cag_name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('goods_name', models.CharField(max_length=30)),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('goods_image', models.ImageField(upload_to='')),
                ('goods_short', models.CharField(max_length=100)),
                ('goods_desc', tinymce.models.HTMLField()),
                ('goods_status', models.BooleanField(default=True)),
                ('goods_unit', models.CharField(max_length=10)),
                ('goods_visit', models.IntegerField(default=0)),
                ('goods_sales', models.IntegerField(default=0)),
                ('goods_cag', models.ForeignKey(to='goods.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
