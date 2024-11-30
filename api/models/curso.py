from django.db import models
from .base import BaseModel
from .categoria import Categoria

class Curso(BaseModel):
    ESTADOS = [(True, "Activo"), (False, "Inactivo")]

    nombre_curso = models.CharField(max_length=255)
    horas_duracion = models.PositiveIntegerField()
    estado = models.BooleanField(choices=ESTADOS, default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name="cursos")

    def __str__(self):
        return self.nombre_curso