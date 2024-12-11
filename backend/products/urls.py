from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_create_view),
    path('<str:pk>/', views.product_detail_view)
]