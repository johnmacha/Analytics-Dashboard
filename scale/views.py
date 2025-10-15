from django.shortcuts import render
from rest_framework import generics
from .models import SiteActivity
from .serializers import SiteActivitySerializer

# Create your views here.
class SiteActivityCreateView(generics.CreateAPIView):
    queryset = SiteActivity.objects.all()
    serializer_class = SiteActivitySerializer