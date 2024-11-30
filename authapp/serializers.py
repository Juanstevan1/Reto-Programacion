# auth/serializers.py
from rest_framework import serializers
from api.models import Usuario  # Importamos desde la app `api`

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'email', 'password']

    def create(self, validated_data):
        # Creamos el usuario utilizando el manager personalizado
        user = Usuario.objects.create_user(
            email=validated_data['email'],
            cedula=validated_data['cedula'],
            password=validated_data['password'],
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            edad=validated_data['edad'],
        )
        return user


class LoginUsuarioSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)