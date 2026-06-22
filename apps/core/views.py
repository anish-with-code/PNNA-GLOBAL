from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ContactMessage
from .forms import ContactForm
from apps.products.models import Product, Category


def home_view(request):
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    categories = Category.objects.all()
    latest_products = Product.objects.filter(is_active=True)[:12]

    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'core/home.html', context)


def about_view(request):
    context = {}
    return render(request, 'core/about.html', context)


@require_http_methods(["GET", "POST"])
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('core:home')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'core/contact.html', context)


@api_view(['GET'])
def api_homepage(request):
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    categories = Category.objects.all().values('id', 'name', 'slug')

    from apps.products.serializers import ProductSerializer
    serializer = ProductSerializer(featured_products, many=True)

    return Response({
        'featured_products': serializer.data,
        'categories': list(categories),
    })


@api_view(['POST'])
def api_contact(request):
    form = ContactForm(request.data)
    if form.is_valid():
        form.save()
        return Response({'message': 'Thank you for contacting us!'}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
