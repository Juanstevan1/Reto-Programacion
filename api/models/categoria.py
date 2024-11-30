from django.db import models
from .base import BaseModel

class Categoria(BaseModel):
    ESTADOS = [(True, "Activo"), (False, "Inactivo")]
    nombre = models.CharField(max_length=255, unique=True)
    estado = models.BooleanField(choices=ESTADOS, default=True)

    def __str__(self):
        return self.nombre
