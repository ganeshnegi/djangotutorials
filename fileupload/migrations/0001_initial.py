# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-27 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=120)),
                ('doc_file', models.FileField(upload_to='document')),
            ],
        ),
    ]
