# Generated by Django 2.0.3 on 2018-04-11 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180411_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='activity',
            name='url',
            field=models.CharField(default='', max_length=128),
        ),
    ]