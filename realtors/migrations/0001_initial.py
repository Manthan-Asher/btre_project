# Generated by Django 3.0.4 on 2020-04-04 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('desc', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('hire_date', models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 4, 20, 26, 13, 374734))),
                ('is_mvp', models.BooleanField(default=False)),
            ],
        ),
    ]
