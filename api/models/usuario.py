from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, cedula, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        if not cedula:
            raise ValueError('El usuario debe tener una cédula')

        email = self.normalize_email(email)
        user = self.model(email=email, cedula=cedula, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cedula, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, cedula, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    ESTADOS = [(True, "Activo"), (False, "Inactivo")]

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.CharField(max_length=15, unique=True)
    edad = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    estado = models.BooleanField(choices=ESTADOS, default=True)
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cedula', 'nombre', 'apellido']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
