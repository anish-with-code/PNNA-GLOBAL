from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .forms import CheckoutForm
from apps.cart.models import Cart, CartItem
from apps.products.models import Product
import uuid


def generate_order_number():
    return f"ORD-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"


@login_required(login_url='users:login')
def checkout_view(request):
    try:
        cart = request.user.cart
    except Cart.DoesNotExist:
        messages.error(request, 'Your cart is empty')
        return redirect('core:home')

    if not cart.items.exists():
        messages.error(request, 'Your cart is empty')
        return redirect('core:home')

    if request.method == 'POST':
        form = CheckoutForm(request.user, request.POST)
        if form.is_valid():
            order = create_order(request.user, cart, form)
            cart.items.all().delete()
            return redirect('orders:order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm(request.user)

    context = {
        'form': form,
        'cart': cart,
        'cart_total': cart.get_cart_total,
    }
    return render(request, 'orders/checkout.html', context)


def create_order(user, cart, form):
    order = Order.objects.create(
        user=user,
        order_number=generate_order_number(),
        shipping_address=form.cleaned_data['shipping_address'],
        payment_method=form.cleaned_data['payment_method'],
        notes=form.cleaned_data.get('notes', ''),
        subtotal=cart.get_cart_total,
        total_amount=cart.get_cart_total + Decimal('50'),
    )

    for cart_item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            price=cart_item.product.discount_price or cart_item.product.price,
        )

    return order


@login_required(login_url='users:login')
def order_confirmation_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    return render(request, 'orders/order_confirmation.html', context)


@login_required(login_url='users:login')
def order_tracking_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    return render(request, 'orders/order_tracking.html', context)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_checkout(request):
    if request.method == 'GET':
        try:
            cart = request.user.cart
            return Response({
                'subtotal': float(cart.get_cart_total),
                'shipping': 50.00,
                'tax': float(cart.get_cart_total * 0.05),
                'total': float(cart.get_cart_total + Decimal('50')),
            })
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        try:
            cart = request.user.cart
            if not cart.items.exists():
                return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

            order = create_order(
                request.user,
                cart,
                type('obj', (object,), {
                    'cleaned_data': {
                        'shipping_address': request.user.addresses.filter(is_default=True).first(),
                        'payment_method': request.data.get('payment_method', 'cod'),
                        'notes': request.data.get('notes', ''),
                    }
                })()
            )

            cart.items.all().delete()
            return Response({
                'message': 'Order created successfully',
                'order_id': order.id,
                'order_number': order.order_number,
            }, status=status.HTTP_201_CREATED)

        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)


from decimal import Decimal
