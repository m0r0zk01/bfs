# Generated by Django 3.1.1 on 2020-10-03 00:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20201003_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 3, 0, 46, 46, 853808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='ce5e5ce29b6e4013812b3638e4bf99f0', max_length=30),
        ),
    ]