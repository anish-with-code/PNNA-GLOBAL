from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Populate the database with PNNA Global products'

    def handle(self, *args, **options):
        # Create categories
        western_cat, _ = Category.objects.get_or_create(
            name='Western',
            defaults={'slug': 'western', 'description': 'Contemporary western jewelry designs'}
        )
        ethnic_cat, _ = Category.objects.get_or_create(
            name='Ethnic',
            defaults={'slug': 'ethnic', 'description': 'Traditional and fusion ethnic jewelry designs'}
        )

        products_data = [
            # Western - Hot Seller
            {
                'name': 'Pearl & Black Crystal Drop Earrings',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Elegant pearl and black crystal drop earrings perfect for any occasion',
                'price': 199,
                'mrp': 399,
                'stock': 50,
                'is_bestseller': True,
                'rating': 4.7,
            },
            # Western - Best Seller
            {
                'name': 'Gold Flower Tassel Drop Earrings',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Beautiful gold flower tassel drop earrings with intricate design',
                'price': 240,
                'mrp': 449,
                'stock': 45,
                'is_bestseller': True,
                'rating': 4.8,
            },
            # Ethnic - New Arrival
            {
                'name': 'Royal Lavender Ghungroo Earrings',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Royal lavender ghungroo earrings with traditional charm',
                'price': 349,
                'mrp': 599,
                'stock': 30,
                'is_new': True,
                'rating': 4.6,
            },
            # Western - Best Value
            {
                'name': '4-Style Earring Combo Pack',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Combo pack of 4 different styles - best value for money',
                'price': 439,
                'mrp': 799,
                'stock': 40,
                'rating': 4.5,
            },
            # Western
            {
                'name': 'White Butterfly Rhinestone Studs',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Cute white butterfly rhinestone stud earrings',
                'price': 199,
                'mrp': 349,
                'stock': 60,
                'rating': 4.4,
            },
            # Western
            {
                'name': 'Gold Arc Crystal Stud Earrings',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Modern gold arc crystal stud earrings',
                'price': 199,
                'mrp': 349,
                'stock': 55,
                'rating': 4.3,
            },
            # Western
            {
                'name': 'Pearl Wing Ear Cuff Earrings',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Stylish pearl wing ear cuff earrings',
                'price': 199,
                'mrp': 349,
                'stock': 50,
                'rating': 4.5,
            },
            # Ethnic - 6 Colors - Turquoise
            {
                'name': 'Silver Arch Chandbali - Turquoise',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Traditional silver arch chandbali with turquoise stones',
                'price': 280,
                'mrp': 499,
                'stock': 35,
                'rating': 4.7,
            },
            # Ethnic - Red
            {
                'name': 'Silver Arch Chandbali - Red',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Traditional silver arch chandbali with red stones',
                'price': 280,
                'mrp': 499,
                'stock': 35,
                'rating': 4.7,
            },
            # Ethnic - Green
            {
                'name': 'Silver Arch Chandbali - Green',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Traditional silver arch chandbali with green stones',
                'price': 280,
                'mrp': 499,
                'stock': 35,
                'rating': 4.7,
            },
            # Ethnic - Black
            {
                'name': 'Silver Arch Chandbali - Black',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Traditional silver arch chandbali with black stones',
                'price': 280,
                'mrp': 499,
                'stock': 35,
                'rating': 4.6,
            },
            # Ethnic - Lavender
            {
                'name': 'Silver Arch Chandbali - Lavender',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Traditional silver arch chandbali with lavender stones',
                'price': 280,
                'mrp': 499,
                'stock': 35,
                'rating': 4.6,
            },
            # Ethnic - Maroon
            {
                'name': 'Silver Arch Chandbali - Maroon',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Traditional silver arch chandbali with maroon stones',
                'price': 280,
                'mrp': 499,
                'stock': 35,
                'rating': 4.6,
            },
            # Ethnic - Best Seller
            {
                'name': 'Antique Pink Jhumka Earrings',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Beautiful antique pink jhumka earrings for special occasions',
                'price': 299,
                'mrp': 549,
                'stock': 40,
                'is_bestseller': True,
                'rating': 4.8,
            },
            # Western - New
            {
                'name': 'Purple Bow Heart Drop Earrings',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Cute purple bow heart drop earrings',
                'price': 160,
                'mrp': 299,
                'stock': 50,
                'is_new': True,
                'rating': 4.3,
            },
            # Western - Hot
            {
                'name': 'White Floral Hoop Crystal Drop',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Elegant white floral hoop crystal drop earrings',
                'price': 220,
                'mrp': 399,
                'stock': 45,
                'is_featured': True,
                'rating': 4.6,
            },
            # Ethnic - Best Seller
            {
                'name': 'Silver Black Onyx Elephant Chandbali',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Unique silver black onyx elephant chandbali earrings',
                'price': 199,
                'mrp': 399,
                'stock': 30,
                'is_bestseller': True,
                'rating': 4.5,
            },
            # Ethnic - Best Seller
            {
                'name': 'Antique Gold Ruby Jhumka Earrings',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Stunning antique gold ruby jhumka earrings',
                'price': 359,
                'mrp': 599,
                'stock': 25,
                'is_bestseller': True,
                'is_featured': True,
                'rating': 4.9,
            },
            # Western - New
            {
                'name': 'Black Rose Gold Bow Drop Earrings',
                'category': western_cat,
                'product_type': 'western',
                'description': 'Trendy black rose gold bow drop earrings',
                'price': 199,
                'mrp': 349,
                'stock': 40,
                'is_new': True,
                'rating': 4.4,
            },
            # Ethnic - New
            {
                'name': 'Antique Gold Turquoise Jhumka',
                'category': ethnic_cat,
                'product_type': 'ethnic',
                'description': 'Exquisite antique gold turquoise jhumka earrings',
                'price': 350,
                'mrp': 599,
                'stock': 28,
                'is_new': True,
                'is_featured': True,
                'rating': 4.8,
            },
        ]

        for product_data in products_data:
            Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'slug': product_data['name'].lower().replace(' ', '-').replace('&', 'and'),
                    'category': product_data['category'],
                    'product_type': product_data['product_type'],
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'mrp': product_data['mrp'],
                    'stock': product_data['stock'],
                    'status': 'available',
                    'is_bestseller': product_data.get('is_bestseller', False),
                    'is_new': product_data.get('is_new', False),
                    'is_featured': product_data.get('is_featured', False),
                    'rating': product_data.get('rating', 4.5),
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated products'))
