from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistroUsuarioSerializer, LoginUsuarioSerializer
from api.models import Usuario 
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Usuario registrado exitosamente",
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Autenticamos al usuario
            user = authenticate(request, email=email, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'message': 'Inicio de sesión exitoso',
                    'token': token.key,
                    'user': {
                        'id': user.id,
                        'nombre': user.nombre,
                        'apellido': user.apellido,
                        'email': user.email,
                    }
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
