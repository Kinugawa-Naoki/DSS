# Generated by Django 3.1.2 on 2020-10-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201023_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverableinfo',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deliverableinfo',
            name='good_num',
            field=models.IntegerField(default=0),
        ),
    ]
