from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(null=True)

    def __str__(self):
        return f"{self.nombre} - {self.precio}"

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.username} - {'Completado' if self.estado else 'Pendiente'}"
