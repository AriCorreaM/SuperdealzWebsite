from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):

    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    id_producto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    nombre = models.TextField()
    descripcion = models.TextField(blank=True)
    medida = models.CharField(max_length=50)
    imagen = models.ImageField(
        upload_to='productos', blank=True, max_length=200)
    url = models.URLField(max_length=500, blank=True)
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(
        Categoria, db_column='id_categoria', on_delete=models.CASCADE)

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.nombre


class Error(models.Model):

    id_error = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    comentarios = models.CharField(max_length=150)
    url = models.URLField(max_length=100)
    producto = models.ForeignKey(
        Producto, db_column='id_producto', on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'error'


class Supermercado(models.Model):
    id_super = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    main_url = models.URLField(max_length=100)
    term_uso = models.URLField(max_length=150)
    logo = models.CharField(max_length=250)
    estado = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'supermercado'


class Precio(models.Model):
    id_precio = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(
        Producto, db_column='id_producto', on_delete=models.CASCADE)
    supermercado = models.ForeignKey(
        Supermercado, db_column='id_super', on_delete=models.CASCADE)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = False
        db_table = 'precio'

    def __str__(self):
        return self.precio


class Listasuper(models.Model):
    id_listasuper = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'listasuper'


class Prodxlista(models.Model):
    id_prodxlista = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(
        Producto, db_column='id_producto', on_delete=models.CASCADE)
    precio = models.ForeignKey(
        Precio, db_column='id_precio', on_delete=models.CASCADE)
    listasuper = models.ForeignKey(
        Listasuper, db_column='id_listasuper', on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'prodxlista'

    def __str__(self):
        return "{} - {}".format(
            self.producto.nombre, self.listasuper.id_usuario.username
        )


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'region'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=50)
    region = models.ForeignKey(
        Region, db_column='id_region', on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'comuna'


class Sucursal(models.Model):

    id_sucursal = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    comuna = models.ForeignKey(
        Comuna, db_column='id_comuna', on_delete=models.CASCADE)
    supermercado = models.ForeignKey(
        Supermercado, db_column='id_super', on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'sucursal'
