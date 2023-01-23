from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets,response
from .models import *
from .serializers import *

# Create your views here.


class CategoryView(viewsets.ViewSet):
    
    query =Catogory.objects.all()
    def list(self,request):
        serializer =CategorySerializer(self.query,many=True)
      
        return response.Response(serializer.data)
  