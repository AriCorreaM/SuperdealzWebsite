# Generated by Django 2.0.9 on 2018-11-23 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superdealzapp', '0005_auto_20181123_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
