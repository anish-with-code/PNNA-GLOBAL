from django.contrib import admin
from .models import Category, Product, ProductImage
from .forms import CategoryForm, ProductForm, ProductImageForm


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    form = ProductImageForm
    extra = 1
    fields = ['image', 'alt_text', 'is_primary']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    form = CategoryForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount_price', 'stock', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    search_fields = ['name', 'description', 'sku']
    prepopulated_fields = {'slug': ('name',)}
    form = ProductForm
    inlines = [ProductImageInline]
    readonly_fields = ['created_at', 'updated_at', 'slug']

    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'slug', 'category', 'sku')
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price')
        }),
        ('Inventory', {
            'fields': ('stock', 'is_active')
        }),
        ('Marketing', {
            'fields': ('is_featured', 'rating')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ['created_at', 'updated_at']
        return self.readonly_fields


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'is_primary', 'created_at']
    list_filter = ['product', 'is_primary', 'created_at']
    search_fields = ['product__name']
    readonly_fields = ['created_at']
    form = ProductImageForm
