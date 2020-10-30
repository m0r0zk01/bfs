# Generated by Django 3.1.1 on 2020-10-30 13:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20201003_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='org',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 13, 22, 52, 731831, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='b84485820ea94e64bf2a3c468fe054df', max_length=30),
        ),
        migrations.AlterField(
            model_name='worker',
            name='work_card',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.card'),
        ),
    ]