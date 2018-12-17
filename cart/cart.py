from decimal import Decimal
from django.conf import settings
from superdealzapp.models import Producto


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, producto, cantidad=1, actualizar_cantidad=False):
        product_id = str(product.id_producto)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'cantidad': 0,
                'precio': str(producto.precio)
            }
        if actualizar_cantidad:
            self.cart[product_id]['cantidad'] = cantidad
        else:
            self.cart[product_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, producto):
        product_id = str(producto.id_producto)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        id_productos = self.cart.keys()
        productos = Producto.objects.filter(id_producto__in=id_productos)
        for producto in productos:
            self.cart[str(producto.id)]['producto'] = producto

        for item in self.cart.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True