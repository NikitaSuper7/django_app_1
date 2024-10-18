from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category


def main_page(request):
    """Рендерит главную страницу"""
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, template_name='catalog/main_page.html', context=context)


def catalog(request):
    """Рендерит страницу каталога"""
    return render(request, template_name="catalog/catalog.html")


def category(request):
    """Рендерит страницу категорий"""
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return render(request, template_name='catalog/category_page.html', context=context)

def index(request):
    product = Product.objects.get(id=1)
    context = {
        'product_name': f"{product.name}",
        'product_price': f"Стоимость продукта - {product.price}",
    }
    return render(request, template_name='catalog/index.html', context=context)

def category_list(request):
    categoryies = Category.objects.all()

    context = {
        'categories': categoryies
    }
    return render(request, template_name='catalog/category_list.html', context=context)



def contact(request):
    """Пример контроллера, обрабатывающий POST-запрос."""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        return HttpResponse(
            f"Спасибо {name.title()}, вы успешно зарегестрированы с почтой -\n'{email}'."
        )
    # Чтобы приложение не падало в ошибку, возвращаем рендер нашего шаблона.
    return render(request, "catalog/contacts.html")

def product_details(request, product_id):
    """Отображает продукт по его ID"""
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }

    return render(request, template_name='catalog/product_info.html', context=context)

