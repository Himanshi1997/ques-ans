# Generated by Django 2.1.15 on 2020-05-19 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0009_auto_20200519_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 10, 36, 31, 271729), editable=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 10, 36, 31, 271757)),
        ),
    ]
