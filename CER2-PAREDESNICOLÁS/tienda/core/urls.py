from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista principal
    path('catalogo/', views.catalogo, name='catalogo'),  # Página del catálogo
    path('formulario/', views.formulario, name='formulario'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),  # Registro de usuario
    path('carrito/', views.carrito, name='carrito'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('actualizar-cantidad/<int:producto_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar-del-carro/<int:producto_id>/', views.eliminar_del_carro, name='eliminar_del_carro'),
    path('realizar-pedido/', views.realizar_pedido, name='realizar_pedido'),
]
