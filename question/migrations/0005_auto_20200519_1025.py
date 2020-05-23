# Generated by Django 2.1.15 on 2020-05-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0008_auto_20200519_1025'),
        ('question', '0004_auto_20200513_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quesdetail',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='QuesDetail',
        ),
    ]
