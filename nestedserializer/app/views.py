from django.shortcuts import render
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets
from .models import Singer, Song

# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    query = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    query = Song.objects.all()
    serializer_class = SongSerializer