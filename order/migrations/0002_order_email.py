# Generated by Django 4.1.3 on 2022-12-05 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=datetime.datetime(2022, 12, 5, 8, 8, 5, 88192, tzinfo=datetime.timezone.utc), max_length=254),
            preserve_default=False,
        ),
    ]