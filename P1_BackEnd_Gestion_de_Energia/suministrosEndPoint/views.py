from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SuministroModel, EtiquetasSuministroModel
from .serializers import SuministroSerializer, EtiquetasSuministroSerializer

class SuministroViewSet(viewsets.ModelViewSet):
    queryset = SuministroModel.objects.all()
    serializer_class = SuministroSerializer

class EtiquetasSuministroViewSet(viewsets.ModelViewSet):
    queryset = EtiquetasSuministroModel.objects.all()
    serializer_class = EtiquetasSuministroSerializer

# Esta vista está basada en viewsets de Django REST Framework, lo cual nos permite
# gestionar de manera fácil y rápida las operaciones CRUD (Crear, Leer, Actualizar, Borrar) 
# para el modelo SuministroModel. Usamos viewsets.ModelViewSet que proporciona 
# implementaciones predeterminadas para los métodos CRUD.
# 
# Importamos los siguientes componentes:
# - viewsets desde rest_framework para crear las vistas CRUD.
# - SuministroModel desde models.py, que define la estructura de nuestros datos.
# - SuministroSerializer desde serializers.py, que maneja la conversión de datos 
#   entre los formatos JSON y el modelo SuministroModel.
# 
# La clase SuministroViewSet define dos atributos clave:
# - queryset: especifica el conjunto de datos que esta vista manejará, en este caso 
#   todos los objetos de SuministroModel.
# - serializer_class: define el serializador que se utilizará para convertir 
#   las instancias del modelo a y desde JSON.

#Operaciones CRUD Disponibles:
#GET /suministros/suministros/:

#Recupera la lista de todos los suministros.
#POST /suministros/suministros/:

#Crea un nuevo suministro.
#GET /suministros/suministros/{id}/:

#Recupera un suministro específico por su ID.
#PUT /suministros/suministros/{id}/:

#Actualiza un suministro