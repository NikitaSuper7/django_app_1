from .models import Category, Product

class ProductServices:

    @staticmethod
    def category_products(category_pk):
        products = Product.objects.filter(category=category_pk)
        return products