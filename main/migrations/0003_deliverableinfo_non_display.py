# Generated by Django 3.1.2 on 2020-10-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pabliccomment_post_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverableinfo',
            name='non_display',
            field=models.CharField(default='off', max_length=6),
        ),
    ]