from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UsuarioViewSet, CategoriaViewSet, CursoViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('categorias', CategoriaViewSet)
router.register('cursos', CursoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token, name='api_token_auth'),  # Endpoint para obtener tokens

]