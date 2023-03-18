from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category="fiction")
    serializer_class = BookSerializer

class SciFiViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='science fiction')
    serializer_class = BookSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='action')
    serializer_class = BookSerializer

class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='mystery')
    serializer_class = BookSerializer

class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='historical fiction')
    serializer_class = BookSerializer

class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='romance')
    serializer_class = BookSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='biography')
    serializer_class = BookSerializer

class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='horror')
    serializer_class = BookSerializer

class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='thriller')
    serializer_class = BookSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Category='history')
    serializer_class = BookSerializer
    