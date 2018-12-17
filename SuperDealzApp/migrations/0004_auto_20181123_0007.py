# Generated by Django 2.0.9 on 2018-11-23 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superdealzapp', '0003_remove_prodxlista_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodxlista',
            name='precio',
            field=models.ForeignKey(db_column='id_precio', default='', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Precio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.TextField(),
        ),
    ]
