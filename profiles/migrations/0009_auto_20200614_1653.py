# Generated by Django 2.2 on 2020-06-14 16:53

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20200613_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=256, null=True, verbose_name='Titre')),
                ('descri', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Information',
                'verbose_name_plural': 'Infromations',
                'db_table': 'Informationss',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='souscriptions',
            name='dateDexpiration',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 16, 53, 28, 674044), verbose_name='Expire le'),
        ),
    ]
