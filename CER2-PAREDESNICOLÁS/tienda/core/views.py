from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import path
from . import views

from .models import Producto, Pedido
from django.contrib.auth.models import User, Group


#-----------------------------------------------------------------------------------------------


def index(request):
    return render(request, 'index.html')

#------------------------------------------------------------------------------

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})

#------------------------------------------------------------------------------

@login_required(login_url='login')
def formulario(request):
    return render(request, 'formulario.html')

#-----------------------------------------------------------------------------

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        c_password = request.POST.get('confirm_password', '')

        if password != c_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado.')
            return render(request, 'register.html')

        user = User.objects.create_user(username = username, email = email, password = password)
        clientes_group = Group.objects.get(name='Usuario')
        user.groups.add(clientes_group)
        user.save()
        messages.success(request, 'Te has registrado exitosamente. Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # Verificar si el nombre de usuario de este usuario coincide con el ingresado
        if user_with_email.username != username:
            messages.error(request, 'El correo y el nombre de usuario no coinciden.')
            
        else:
            # Autenticar con el nombre de usuario y la contraseña
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Si la autenticación es exitosa, iniciar sesión
                auth_login(request, user)
                messages.success(request, f'Bienvenido, {user.username}')
                return redirect('index')
            else:
                # Contraseña incorrecta
                messages.error(request, 'Contraseña incorrecta.')

    return render(request, 'login.html')

#----------------------------------------------------------------------------------------

@login_required(login_url='login')
def carrito(request):
    carrito = request.session.get('carrito', {})
    for item in carrito.values():
        item['total'] = item['precio'] * item['cantidad']
    total_general = sum(item['total'] for item in carrito.values())
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total_general})

# Agregar producto al carrito
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto = get_object_or_404(Producto, id=producto_id)
    str_producto_id = str(producto_id)
    if str_producto_id in carrito:
        carrito[str_producto_id]['cantidad'] += 1
    else:
        carrito[str_producto_id] = {
            'nombre': producto.nombre,
            'precio': producto.precio,
            'cantidad': 1,
        }
    request.session['carrito'] = carrito
    return redirect('catalogo')

# Actualizar cantidad de un producto en el carrito
def actualizar_cantidad(request, producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        carrito = request.session.get('carrito', {})
        str_producto_id = str(producto_id)
        if str_producto_id in carrito and cantidad > 0:
            carrito[str_producto_id]['cantidad'] = cantidad
            request.session['carrito'] = carrito
    return redirect('carrito')

# Eliminar producto del carrito
def eliminar_del_carro(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito
    return redirect('carrito')

# Realizar el pedido
@login_required(login_url='login')
def realizar_pedido(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('catalogo')

    pedido = Pedido.objects.create(usuario=request.user)
    request.session['carrito'] = {}  # Limpia carrito
    messages.success(request, "Tu pedido ha sido realizado exitosamente.")
    return redirect('carrito')

# Create your views here.


