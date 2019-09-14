# Generated by Django 2.2.5 on 2019-09-14 16:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0008_auto_20190914_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrape',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 16, 0, 35, 587058, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='last_update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 16, 0, 35, 587223, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 16, 0, 35, 587000, tzinfo=utc)),
        ),
    ]