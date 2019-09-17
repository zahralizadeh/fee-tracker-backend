# Generated by Django 2.2.5 on 2019-09-17 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0011_auto_20190915_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyfile',
            name='offertype',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 17, 8, 29, 43, 864847, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='last_update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 17, 8, 29, 43, 865052, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scrape',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 17, 8, 29, 43, 686158, tzinfo=utc)),
        ),
    ]
