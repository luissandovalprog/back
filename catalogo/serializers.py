from rest_framework import serializers
from .models import Autor, Libro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(source='autor.__str__', read_only=True)
    
    class Meta:
        model = Libro
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['autor_detalle'] = {
            'id': instance.autor.id,
            'nombre_completo': str(instance.autor),
            'nombre': instance.autor.nombre,
            'apellido': instance.autor.apellido
        }
        return representation