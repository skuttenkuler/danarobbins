from django.shortcuts import render
from .models import Gig
from .serializers import GigSerializer
from rest_framework import generics
# Create your views here.

class GigList(generics.ListCreateAPIView):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer