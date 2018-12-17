from django.conf.urls import url, include
from .views import *
from . import views
from django.contrib.auth.views import (
    login, logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

app_name = 'superdealzapp'

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    #URLs Account
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^registro/$', views.register, name='register'),
    url(r'^mi-perfil/$', views.view_profile, name='view_profile'),
    url(r'^mi-perfil/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^cambiar-pass/$', views.change_password, name='change_password'),

    url(r'^reset-pass/$', password_reset,  name='reset_password'),
    url(r'^reset-pass/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-pass/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-pass/complete/$', password_reset_complete,
        {'template_name': 'accounts/reset_password_complete.html'},
        name='password_reset_complete'),

    url(r'^productos$', views.pagina_productos, name="productos"),
    url(r'^comparar_productos$', views.comparar_precios),
    url(r'^acerca_nosotros$', views.acerca_nosotros),
    url(r'^mis-listas$', views.mis_listas),
    # url(r'^destacados$', views.destacados),
    # url(r'^notificaciones$', views.notificaciones),)
    url(r'^error$', views.error),
    url(r'^contacto$', views.contacto),
    # url(r'^cuenta$', views.mi_cuenta),
]
