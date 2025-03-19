from rest_framework.serializers import ModelSerializer
from .models import Filme, FilmeAssistido

class FilmeSerializer(ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'
        
class FilmeAssistidoSerializer(ModelSerializer):
    class Meta:
        model = FilmeAssistido
        fields = '__all__'