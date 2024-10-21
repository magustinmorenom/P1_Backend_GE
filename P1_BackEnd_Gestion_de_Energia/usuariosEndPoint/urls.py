# usuariosEndPoint/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import usuariosModelViewSet

router = DefaultRouter()
router.register(r'usuarios', usuariosModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]