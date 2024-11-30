from rest_framework.test import APITestCase
from api.models import Usuario


class UsuarioAPITestCase(APITestCase):

    def test_crear_usuario(self):
        data = {
            "nombre": "Juan",
            "apellido": "Garcia",
            "cedula": "123456789",
            "edad": 30,
            "email": "kazodroid@gmail.com",
            "estado": True
        }
        response = self.client.post('/api/usuarios/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Usuario.objects.count(), 1)