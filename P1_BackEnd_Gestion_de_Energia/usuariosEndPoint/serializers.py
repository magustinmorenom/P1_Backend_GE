from rest_framework import serializers
from .models import usuariosModel

class usuariosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuariosModel
        fields = '__all__'