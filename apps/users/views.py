from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, UserProfile, Address
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileForm, AddressForm, LoginForm
from apps.orders.models import Order


@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('users:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(1209600)
                messages.success(request, f'Welcome back, {user.first_name}!')
                return redirect(request.GET.get('next', 'core:home'))
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required(login_url='users:login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('core:home')


@login_required(login_url='users:login')
def profile_view(request):
    profile = request.user.profile
    addresses = request.user.addresses.all()

    context = {
        'profile': profile,
        'addresses': addresses,
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='users:login')
@require_http_methods(["GET", "POST"])
def edit_profile_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('users:profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/edit_profile.html', context)


@login_required(login_url='users:login')
def order_history_view(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    context = {'orders': orders}
    return render(request, 'users/order_history.html', context)


@login_required(login_url='users:login')
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    return render(request, 'users/order_detail.html', context)


@login_required(login_url='users:login')
def wishlist_view(request):
    wishlist = request.user.profile.wishlist.all()
    context = {'wishlist_items': wishlist}
    return render(request, 'users/wishlist.html', context)


@login_required(login_url='users:login')
@require_http_methods(["GET", "POST"])
def manage_addresses_view(request, address_id=None):
    if address_id:
        address = get_object_or_404(Address, id=address_id, user=request.user)
    else:
        address = None

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, 'Address saved successfully.')
            return redirect('users:profile')
    else:
        form = AddressForm(instance=address)

    context = {'form': form, 'address': address}
    return render(request, 'users/manage_address.html', context)


@login_required(login_url='users:login')
def delete_address_view(request, address_id):
    address = get_object_or_404(Address, id=address_id, user=request.user)
    if request.method == 'POST':
        address.delete()
        messages.success(request, 'Address deleted successfully.')
    return redirect('users:profile')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_user_profile(request):
    user = request.user
    data = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user.phone,
        'is_verified': user.is_verified,
    }
    return Response(data)


@api_view(['POST'])
def api_register(request):
    form = CustomUserCreationForm(request.data)
    if form.is_valid():
        user = form.save()
        UserProfile.objects.create(user=user)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
