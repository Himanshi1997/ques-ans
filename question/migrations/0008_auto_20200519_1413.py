# Generated by Django 2.1.15 on 2020-05-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_auto_20200519_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
