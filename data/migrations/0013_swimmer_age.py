# Generated by Django 3.0.5 on 2020-05-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_remove_swimmer_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='swimmer',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
