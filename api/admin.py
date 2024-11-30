from django.contrib import admin
from .models import Usuario, Curso, Categoria

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'estado')
    search_fields = ('id', 'nombre', 'apellido', 'cedula', 'email')
    list_filter = ('estado',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_curso', 'horas_duracion', 'estado', 'categoria', 'creado_en')
    search_fields = ('id', 'nombre_curso',)
    list_filter = ('estado', 'categoria')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'estado', 'creado_en')
    search_fields = ('id', 'nombre',)
    list_filter = ('estado',)
