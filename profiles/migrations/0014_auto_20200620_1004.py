# Generated by Django 2.2 on 2020-06-20 10:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20200614_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souscriptions',
            name='dateDexpiration',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 10, 4, 39, 640702), verbose_name='Expire le'),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('stripe_id', models.CharField(blank=True, max_length=30)),
                ('user_rec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile', verbose_name='Souscripteur')),
            ],
            options={
                'verbose_name_plural': 'subscribers',
            },
        ),
    ]
