# Generated by Django 3.0.5 on 2020-05-02 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20200501_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='swimmer',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 21, 57, 18, 414299)),
        ),
    ]
