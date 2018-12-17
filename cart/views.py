from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from superdealzapp.models import Producto
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, id_producto):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=id_producto)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(producto=producto, cantidad=cd['cantidad'], actualizar_cantidad=cd['actualizar'])
    return redirect('cart:cart_detail')


def cart_remove(request, id_producto):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=id_producto)
    cart.remove(producto)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'cantidad': item['cantidad'], 'actualizar': True})
    return render(request, 'cart/detail.html', {'cart': cart})