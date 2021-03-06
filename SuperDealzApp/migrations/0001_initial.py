# Generated by Django 2.0.4 on 2018-05-01 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comuna',
            },
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id_error', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('comentarios', models.CharField(max_length=150)),
                ('url', models.URLField(max_length=100)),
            ],
            options={
                'db_table': 'error',
            },
        ),
        migrations.CreateModel(
            name='Listasuper',
            fields=[
                ('id_listasuper', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'listasuper',
            },
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id_precio', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'precio',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=150)),
                ('medida', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, upload_to='productos')),
                ('url', models.URLField(blank=True, max_length=100)),
                ('disponible', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Categoria')),
            ],
            options={
                'db_table': 'producto',
            },
        ),
        migrations.CreateModel(
            name='Prodxlista',
            fields=[
                ('id_prodxlista', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('listasuper', models.ForeignKey(db_column='id_listasuper', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Listasuper')),
                ('precio', models.ForeignKey(db_column='id_precio', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Precio')),
                ('producto', models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Producto')),
            ],
            options={
                'db_table': 'prodxlista',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('comuna', models.ForeignKey(db_column='id_comuna', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Comuna')),
            ],
            options={
                'db_table': 'sucursal',
            },
        ),
        migrations.CreateModel(
            name='Supermercado',
            fields=[
                ('id_super', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('main_url', models.URLField(max_length=100)),
                ('term_uso', models.URLField(max_length=150)),
                ('logo', models.CharField(max_length=250)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'supermercado',
            },
        ),
        migrations.AddField(
            model_name='sucursal',
            name='supermercado',
            field=models.ForeignKey(db_column='id_super', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Supermercado'),
        ),
        migrations.AddField(
            model_name='precio',
            name='producto',
            field=models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Producto'),
        ),
        migrations.AddField(
            model_name='precio',
            name='supermercado',
            field=models.ForeignKey(db_column='id_super', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Supermercado'),
        ),
        migrations.AddField(
            model_name='error',
            name='producto',
            field=models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Producto'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(db_column='id_region', on_delete=django.db.models.deletion.CASCADE, to='superdealzapp.Region'),
        ),
    ]
