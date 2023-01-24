from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets,response
from .models import *
from .serializers import *
from drf_spectacular.utils import extend_schema

# Create your views here.


class CategoryView(viewsets.ViewSet):
    
    query =Catogory.objects.all()
    @extend_schema(responses=CategorySerializer)
    def list(self,request):
        serializer =CategorySerializer(self.query,many=True)
      
        return response.Response(serializer.data)
  