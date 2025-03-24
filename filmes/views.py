from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Filme
from .serializers import FilmeSerializer

class FilterFilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["Title","Watched"]
    search_fields = ["Watched"]
    
    
