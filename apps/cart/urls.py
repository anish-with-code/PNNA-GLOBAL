from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.api_cart, name='api_cart'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('item/<int:item_id>/update/', views.update_cart_item, name='update_item'),
    path('item/<int:item_id>/remove/', views.remove_from_cart, name='remove_item'),
    path('clear/', views.clear_cart, name='clear_cart'),
]
