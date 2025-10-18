from django.shortcuts import render
# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SiteActivity
# from .serializers import SiteActivitySerializer

# Create your views here.
@api_view(['POST'])
def create_activity(request):
    if request.method == 'POST':
        #log the activity
        return Response({'message': 'Activity logged'})
  