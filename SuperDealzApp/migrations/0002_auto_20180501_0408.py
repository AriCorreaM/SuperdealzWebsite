# Generated by Django 2.0.4 on 2018-05-01 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superdealzapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, max_length=150, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='url',
            field=models.URLField(blank=True, max_length=150),
        ),
    ]
