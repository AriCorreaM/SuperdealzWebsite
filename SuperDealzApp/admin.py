from django.contrib import admin
from .models import Producto, Categoria


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['nombre']


class ProductoAdmin(admin.ModelAdmin):

    list_display = [
        'nombre', 'marca', 'medida', 'disponible'
    ]


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
