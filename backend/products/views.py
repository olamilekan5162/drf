from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
  
class ProductDetailApiView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_detail_view = ProductDetailApiView.as_view()

class ProductListCreateApiView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_list_create_view = ProductListCreateApiView.as_view()