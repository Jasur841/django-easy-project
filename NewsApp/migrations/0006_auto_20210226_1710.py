# Generated by Django 3.1.5 on 2021-02-26 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0005_auto_20210108_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 2, 26, 14, 10, 15, 757955, tzinfo=utc)),
        ),
    ]