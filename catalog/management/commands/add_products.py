from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Add test products"

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(category_name='Test_category',
                                                     category_description='test_description')
        products = [
            {'name':"test_name_1", 'description':"test_desc_1", 'image':'', 'price':10_000, 'created_at':"1990-01-01", 'updated_at':"2000-01-01", 'category':category},
            {'name': "test_name_2", 'description': "test_desc_2", 'image': '', 'price': 20_000,
             'created_at': "1992-02-02", 'updated_at': "2002-02-02", 'category': category},
            {'name': "test_name_3", 'description': "test_desc_3", 'image': '', 'price': 30_000,
             'created_at': "1993-03-03", 'updated_at': "2003-03-03", 'category': category},
        ]

        for prod_data in products:
            product, created = Product.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added Product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exists: {product.name}"))