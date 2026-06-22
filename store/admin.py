from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage, Cart, CartItem, Order, OrderItem, Wishlist

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    ordering = ['name']

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text', 'is_primary']
    ordering = ['-is_primary', 'created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'product_type', 'price', 'mrp', 'discount_badge', 'stock', 'status', 'is_featured', 'is_bestseller', 'is_new', 'created_at']
    list_filter = ['category', 'product_type', 'status', 'is_featured', 'is_bestseller', 'is_new', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProductImageInline]
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'slug', 'category', 'product_type', 'description')
        }),
        ('Pricing', {
            'fields': ('price', 'mrp')
        }),
        ('Inventory', {
            'fields': ('stock', 'status')
        }),
        ('Promotion', {
            'fields': ('is_featured', 'is_bestseller', 'is_new', 'rating')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def discount_badge(self, obj):
        discount = obj.discount_percentage
        if discount > 0:
            return format_html(
                '<span style="background-color: #ff6b6b; color: white; padding: 3px 8px; border-radius: 3px; font-weight: bold;">{}%</span>',
                discount
            )
        return '-'
    discount_badge.short_description = 'Discount'

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['get_product_name', 'image_tag', 'is_primary', 'created_at']
    list_filter = ['product', 'is_primary', 'created_at']
    search_fields = ['product__name']

    def get_product_name(self, obj):
        return obj.product.name
    get_product_name.short_description = 'Product'

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return '-'
    image_tag.short_description = 'Image'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_total_items', 'get_total_price', 'updated_at']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at']

    def get_total_items(self, obj):
        return obj.total_items
    get_total_items.short_description = 'Total Items'

    def get_total_price(self, obj):
        return f"₹{obj.total_price}"
    get_total_price.short_description = 'Total Price'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price', 'subtotal']
    can_delete = False
    fields = ['product', 'quantity', 'price', 'subtotal']

    def subtotal(self, obj):
        return f"₹{obj.subtotal}"
    subtotal.short_description = 'Subtotal'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'get_total', 'status', 'payment_method', 'created_at']
    list_filter = ['status', 'payment_method', 'created_at']
    search_fields = ['order_number', 'user__username', 'user__email', 'email']
    readonly_fields = ['order_number', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'status')
        }),
        ('Delivery Details', {
            'fields': ('full_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code')
        }),
        ('Payment', {
            'fields': ('total_amount', 'payment_method')
        }),
        ('Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_total(self, obj):
        return f"₹{obj.total_amount}"
    get_total.short_description = 'Total'

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_product_count', 'updated_at']
    search_fields = ['user__username', 'user__email']
    filter_horizontal = ['products']

    def get_product_count(self, obj):
        return obj.products.count()
    get_product_count.short_description = 'Products in Wishlist'
