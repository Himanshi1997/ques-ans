# Generated by Django 2.1.15 on 2020-05-13 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ansdetail',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='ansdetail',
            name='rating',
        ),
    ]
