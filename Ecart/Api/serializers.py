from rest_framework import serializers
from owner.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'