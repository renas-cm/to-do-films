from rest_framework.serializers import ModelSerializer
from .models import Filme

class FilmeSerializer(ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'