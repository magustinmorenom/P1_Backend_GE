from rest_framework import serializers
from .models import SuministroModel , EtiquetasSuministroModel

class SuministroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuministroModel
        fields = '__all__'
        
class EtiquetasSuministroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtiquetasSuministroModel
        fields = '__all__'