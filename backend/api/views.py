from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.
@api_view(["POST"])
def api_home (request, *args, **kwargs):
   serializer = ProductSerializer(data=request.data)
   if serializer.is_valid():
     serializer.save()
     return Response(serializer.data)

@api_view(["GET"])
def api_by_id(request, pk):
  instance = Product.objects.get(id=pk)
  data = {}
  if instance:
    data = ProductSerializer(instance).data
    return Response(data)