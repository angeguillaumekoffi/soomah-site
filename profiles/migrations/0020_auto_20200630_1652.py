# Generated by Django 2.2 on 2020-06-30 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20200630_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souscriptions',
            name='dateDexpiration',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 16, 52, 51, 190715), verbose_name='Expire le'),
        ),
    ]
