from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuministroViewSet , EtiquetasSuministroViewSet

router = DefaultRouter()
router.register(r'suministros', SuministroViewSet, basename='suministro')
router.register(r'etiquetas_suministros', EtiquetasSuministroViewSet, basename='etiquetas_suministro')

urlpatterns = [
    path('', include(router.urls)),
]
