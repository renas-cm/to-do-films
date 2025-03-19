from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Filme, FilmeAssistido
from .serializers import FilmeSerializer, FilmeAssistidoSerializer

class FilmeViewSet(ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    
class FilmeAssistidoViewSet(ModelViewSet):
    queryset = FilmeAssistido.objects.all()
    serializer_class = FilmeAssistidoSerializer
