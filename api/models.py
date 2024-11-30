from django.db import models

class Usuario(models.Model):
    ESTADOS = [
        (True, "Activo"),
        (False, "Inactivo")
    ]

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.CharField(max_length=15, unique=True)
    edad = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    estado = models.BooleanField(choices=ESTADOS, default=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"