from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('products/<str:pk>/', views.api_by_id)
]