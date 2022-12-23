from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemsList.as_view(), name='item_list'),
    path('item/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
]
