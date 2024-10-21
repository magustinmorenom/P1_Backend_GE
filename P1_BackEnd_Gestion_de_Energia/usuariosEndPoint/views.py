# usuariosEndPoint/views.py
from rest_framework import viewsets
from .models import usuariosModel
from .serializers import usuariosModelSerializer

class usuariosModelViewSet(viewsets.ModelViewSet):
    queryset = usuariosModel.objects.all()
    serializer_class = usuariosModelSerializer