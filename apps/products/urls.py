from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.api_products, name='api_list'),
    path('categories/', views.api_categories, name='api_categories'),
    path('featured/', views.api_featured_products, name='api_featured'),
    path('<slug:slug>/', views.api_product_detail, name='api_detail'),
]
