from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Catogory
        fields = '__all__'       