from django.shortcuts import render, redirect
from django.http import HttpResponse
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# from .forms import ProductForm
last_page = 1


class MainView(ListView):
    model = Product
    template_name = 'catalog/main_page.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context_data['products'] = [products[i:i + 9] for i in range(0, len(products), 9)]
        if self.request.method == "GET":
            page = self.request.GET.get('page')
            global last_page
            if page in ['1', '2', '3']:
                last_page = int(page)
                context_data['products'] = context_data['products'][int(last_page) - 1]
            elif page == 'Previous' and last_page > 1:
                last_page -= 1
                context_data['products'] = context_data['products'][int(last_page) - 1]
            elif page == 'Previous' and last_page <= 1:
                context_data['products'] = context_data['products'][int(last_page) - 1]
            elif page == 'Next' and last_page < len(context_data['products']) - 1:
                last_page += 1
                context_data['products'] = context_data['products'][int(last_page) - 1]
            elif page == 'Next':
                context_data['products'] = context_data['products'][int(last_page) - 1]
            else:
                context_data['products'] = context_data['products'][1]
            # print(f"Page - {page}")
        print(f"Длина контекста - {len(context_data['products'])}")
        print(context_data)
        return context_data


# def main_page(request):
#     """Рендерит главную страницу"""
#     products = Product.objects.all()
#     page = '1' if request.GET.get('page') is None else request.GET.get('page')
#     pages = [products[i:i + 9] for i in range(0, len(products), 9)]
#     global last_page
#
#     if page in ['1', '2', '3']:
#         last_page = int(page)
#         show_page = pages[int(last_page) - 1]
#     elif page == 'Previous' and last_page > 1:
#         last_page -= 1
#         show_page = pages[int(last_page) - 1]
#     elif page == 'Previous' and last_page <= 1:
#         show_page = pages[int(last_page) - 1]
#     elif page == 'Next' and last_page < len(pages) - 1:
#         last_page += 1
#         show_page = pages[int(last_page) - 1]
#     elif page == 'Next':
#         show_page = pages[int(last_page) - 1]
#     else:
#         show_page = pages[1]
#
#     context = {
#         'products': products,
#         'page': page,
#         'show_page': show_page,
#         'last_page': last_page
#     }
#
#     return render(request, template_name='catalog/main_page.html', context=context)


class CatalogView(ListView):
    model = Product
    template_name = 'catalog/catalog.html'


# def catalog(request):
#     """Рендерит страницу каталога"""
#     return render(request, template_name="catalog/catalog.html")


class CategoryView(ListView):
    model = Category
    template_name = 'catalog/category_page.html'
    context_object_name = 'categories'


# def category(request):
#     """Рендерит страницу категорий"""
#     categories = Category.objects.all()
#     context = {
#         'categories': categories
#     }
#
#     return render(request, template_name='catalog/category_page.html', context=context)


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            print(f'Вы успешно зарегестрированы {name}({email})')

            return HttpResponse(
                        f"Спасибо {name.title()}, вы успешно зарегестрированы с почтой -\n'{email}'."
                    )



class SuccesTemplateView(TemplateView):
    template_name = "catalog/success_reg.html"


# def contact(request):
#     """Пример контроллера, обрабатывающий POST-запрос."""
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#
#         return HttpResponse(
#             f"Спасибо {name.title()}, вы успешно зарегестрированы с почтой -\n'{email}'."
#         )
#     # Чтобы приложение не падало в ошибку, возвращаем рендер нашего шаблона.
#     return render(request, "catalog/contacts.html")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'


# def product_details(request, product_id):
#     """Отображает продукт по его ID"""
#     product = Product.objects.get(id=product_id)
#     context = {
#         'product': product
#     }
#
#     return render(request, template_name='catalog/product_info.html', context=context)

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price', 'videos']
    template_name = 'catalog/add_products.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:success')

# def add_products(request):
#     """Пример контроллера, обрабатывающий POST-запрос."""
#     categories_prod = Category.objects.all()
#     context = {
#         'categories': categories_prod
#     }
#     if request.method == "POST":
#         name = request.POST.get("product_name")
#         product_category = request.POST.get("category_name")
#         product_price = request.POST.get("product_price")
#         product_description = request.POST.get("product_description")
#         product_created_at = request.POST.get("product_created_at")
#         product_updated_at = request.POST.get("product_updated_at")
#
#         form = Product.objects.create(name=name,
#                                       description=product_description,
#                                       category=Category.objects.get(category_name=product_category),
#                                       price=product_price,
#                                       created_at=product_created_at,
#                                       updated_at=product_updated_at,
#                                       image=request.FILES.get('images')
#                                       )
#         form.save()
#         return HttpResponse("Продукт успешно добавлен")
#
#     return render(request, "catalog/add_products.html", context=context)

# def success(request):
#     return HttpResponse('successfully uploaded')
