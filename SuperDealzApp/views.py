from django.shortcuts import render, redirect
from django.db.models import Q  # , Prefetch
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.urls import reverse
from django.contrib.auth import (
    update_session_auth_hash, login, authenticate
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    PasswordChangeForm
)
# from cart.forms import CartAddProductForm
# from fuzzywuzzy import fuzz, process
# from haystack.generic_views import SearchView
from .forms import (
    RegistrationForm, EditProfileForm
)
from .models import (
    Producto, Prodxlista, Precio
)


def inicio(request):

    lista_productos = Producto.objects.all()[:3]

    context = {
        'lista_productos': lista_productos
    }

    return render(request, 'bootstrap3/inicio.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(view_profile)
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def view_profile(request):
    listas = Prodxlista.objects.all()

    form = EditProfileForm(data=request.POST or None, instance=request.user)

    if request.POST and form.is_valid():
        form.save()
        return redirect('superdealz:view_profile')

    context = {
        'form': form,
        'listas': listas
    }

    return render(request, 'accounts/my_profile.html', context)


@login_required
def change_password(request):
    listas = Prodxlista.objects.all()

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, _('Su contraseña fue actualizada con éxito!'))
            return redirect(reverse(view_profile))
        else:
            messages.error(request, _('Por favor corriga los errores.'))
            return redirect(reverse(change_password))
    else:
        form = PasswordChangeForm(user=request.user)

    context = {
        'form': form,
        'listas': listas
    }

    return render(request, 'accounts/change_password.html', context)


def pagina_productos(request):

    list_precios = Precio.objects.\
        select_related('producto', 'supermercado').\
        all()

    search = request.GET.get('q', '')

    if search:
        list_precios = list_precios.\
            filter(
                Q(producto__nombre__icontains=search) |
                Q(producto__marca__icontains=search) |
                Q(producto__categoria__nombre__icontains=search),
            )

    page = request.GET.get('page', 1)
    paginator = Paginator(list_precios, 6)

    try:
        precios = paginator.page(page)
    except PageNotAnInteger:
        precios = paginator.page(1)
    except EmptyPage:
        precios = paginator.page(paginator.num_pages)

    context = {
        'precios': precios,
        'search': search,
    }

    return render(request, 'bootstrap3/pagina_productos.html', context)


def comparar_precios(request):

    comparar = Prodxlista.objects.all()

    for item in comparar:
        matching_results = Producto.objects.\
            filter(
                Q(producto__nombre__icontains=item.producto.nombre) |
                Q(producto__marca__icontains=item.producto.marca)
            )

    context = {
        'comparar': comparar,
        # 'lowest_price': lowest_price,
        # 'lowest_super': lowest_super,
        'matching_results': matching_results
    }

    return render(request, 'bootstrap3/comparar.html', context)


@login_required
def mis_listas(request):
    listas = Prodxlista.objects.all()
    # productos = Producto.objects.all()

    return render(request, 'bootstrap3/mis_listas.html', {'listas': listas})


def error(request):
    return render(request, 'bootstrap3/404_error.html', {})


def acerca_nosotros(request):
    return render(request, 'bootstrap3/acerca_nosotros.html', {})


def contacto(request):
    return render(request, 'bootstrap3/contacto.html', {})
