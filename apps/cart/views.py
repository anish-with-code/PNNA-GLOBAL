from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from apps.products.models import Product


@login_required(login_url='users:login')
def cart_view(request):
    try:
        cart = request.user.cart
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    context = {'cart': cart}
    return render(request, 'cart/cart.html', context)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_cart(request):
    try:
        cart = request.user.cart
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    if request.method == 'GET':
        items_data = []
        for item in cart.items.all():
            items_data.append({
                'id': item.id,
                'product_id': item.product.id,
                'product_name': item.product.name,
                'price': float(item.product.discount_price or item.product.price),
                'quantity': item.quantity,
                'total': float(item.get_total),
                'image': item.product.images.filter(is_primary=True).first().image.url if item.product.images.exists() else '',
            })

        return Response({
            'items': items_data,
            'cart_total': float(cart.get_cart_total),
            'item_count': cart.get_cart_item_count,
        })

    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    try:
        cart = request.user.cart
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if quantity < 1 or quantity > product.stock:
        return Response({'error': 'Invalid quantity'}, status=status.HTTP_400_BAD_REQUEST)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
        if cart_item.quantity > product.stock:
            cart_item.quantity = product.stock
        cart_item.save()

    return Response({
        'message': 'Product added to cart',
        'item_count': cart.get_cart_item_count,
        'cart_total': float(cart.get_cart_total),
    })


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart_item(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, cart=request.user.cart)
    except CartItem.DoesNotExist:
        return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

    quantity = int(request.data.get('quantity', 1))

    if quantity < 1:
        cart_item.delete()
        return Response({
            'message': 'Item removed from cart',
            'item_count': request.user.cart.get_cart_item_count,
            'cart_total': float(request.user.cart.get_cart_total),
        })

    if quantity > cart_item.product.stock:
        return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)

    cart_item.quantity = quantity
    cart_item.save()

    return Response({
        'message': 'Cart item updated',
        'item_count': request.user.cart.get_cart_item_count,
        'cart_total': float(request.user.cart.get_cart_total),
    })


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id, cart=request.user.cart)
    except CartItem.DoesNotExist:
        return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

    cart_item.delete()

    return Response({
        'message': 'Item removed from cart',
        'item_count': request.user.cart.get_cart_item_count,
        'cart_total': float(request.user.cart.get_cart_total),
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def clear_cart(request):
    try:
        cart = request.user.cart
        cart.items.all().delete()
        return Response({'message': 'Cart cleared successfully'})
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)


def cart_context(request):
    if request.user.is_authenticated:
        try:
            cart = request.user.cart
            return {'cart': cart}
        except Cart.DoesNotExist:
            return {'cart': None}
    return {'cart': None}
