# Generated by Django 2.0.3 on 2018-04-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_authenticate',
            field=models.BooleanField(default=False),
        ),
    ]
