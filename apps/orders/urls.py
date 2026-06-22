from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('confirmation/<int:order_id>/', views.order_confirmation_view, name='order_confirmation'),
    path('tracking/<int:order_id>/', views.order_tracking_view, name='order_tracking'),
    path('api/checkout/', views.api_checkout, name='api_checkout'),
]
