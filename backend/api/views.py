from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def api_home (request, *args, **kwargs):
   model_data = Product.objects.all().order_by("?").first()
   data = {}
   if model_data:
    data = model_to_dict(model_data)
    return Response(data)

@api_view(["GET"])
def api_by_id(request, pk):
  model_data = Product.objects.get(id=pk)
  data = {}
  if model_data:
   data = model_to_dict(model_data)
   return Response(data)