# Generated by Django 3.1.4 on 2022-12-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0005_auto_20221207_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='to',
            field=models.TextField(default='default'),
        ),
    ]
