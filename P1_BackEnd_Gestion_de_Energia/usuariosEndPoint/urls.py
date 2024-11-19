# usuariosEndPoint/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import usuariosModelViewSet
from usuariosEndPoint.email_sender.email_alta_reset import send_credentials

router = DefaultRouter()
router.register(r'usuarios', usuariosModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send_credentials/', send_credentials, name='send_credentials'),
]