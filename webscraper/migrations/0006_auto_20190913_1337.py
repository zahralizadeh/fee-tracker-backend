# Generated by Django 2.2.4 on 2019-09-13 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0005_auto_20190913_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrape',
            name='resultnumber',
        ),
        migrations.AlterField(
            model_name='scrape',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
