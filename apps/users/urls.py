from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('orders/', views.order_history_view, name='order_history'),
    path('orders/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('addresses/manage/', views.manage_addresses_view, name='manage_addresses'),
    path('addresses/<int:address_id>/edit/', views.manage_addresses_view, name='edit_address'),
    path('addresses/<int:address_id>/delete/', views.delete_address_view, name='delete_address'),
    path('api/profile/', views.api_user_profile, name='api_profile'),
    path('api/register/', views.api_register, name='api_register'),
]
