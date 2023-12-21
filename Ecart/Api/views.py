from django.shortcuts import render
from owner.models import *
from Api.serializers import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework import authentication, permissions


class CategoryViewSetView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()
    
    def get_product(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        category=Categories.objects.get(id=id)
        product=category.products_set.all()
        serializer=ProductSerializer(product,many=True)
        return Response(data=serializer.data)


class ProductViewSetView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def list(self, request, *args, **kwargs):
        qs = Products.objects.all()
        serializer = ProductSerializer(qs, many=True)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        serializer = ProductSerializer(data=request.data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        product.delete()
        return Response("product deleted", status=status.HTTP_204_NO_CONTENT)


