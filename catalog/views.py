from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect

from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import os
from .forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Для кеширования страниц:
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Для низкоуровневого кеширования:
from django.core.cache import cache

#Сервисный функционал:
from .services import ProductServices

last_page = 1


class MainView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/main_page.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = cache.get('products_queryset')

        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)
        return queryset

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
        #     # print(f"Page - {page}")
        # print(f"Длина контекста - {len(context_data['products'])}")
        # print(context_data)
        return context_data

class CategryProductListView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'catalog/prod_category.html'
    context_object_name = 'category'

    def get_context_data(self,  **kwargs):
        context_data = super().get_context_data()
        category = self.object.pk
        # products = Product.objects.filter(category=category)
        context_data['products'] = ProductServices.category_products(category_pk=category)
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


class CatalogView(LoginRequiredMixin, ListView):
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
    template_name = "catalog/success.html"


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

@method_decorator(cache_page(16 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'


class VideoView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_info_test.html'
    context_object_name = 'video'

    def get(self, request, *args, **kwargs):
        # Получаем объект видео
        self.object = self.get_object()
        file_path = self.object.videos.path

        # Проверка существования файла
        if not os.path.exists(file_path):
            raise Http404("Видео не найдено")

        # Получаем заголовок Range для поддержки перемотки
        range_header = request.headers.get('Range')
        if not range_header:
            return HttpResponse(open(file_path, 'rb'), content_type='video/mp4')

        # Обрабатываем заголовок Range
        start, end = range_header.replace("bytes=", "").split("-")
        file_size = os.path.getsize(file_path)
        start = int(start) if start else 0
        end = int(end) if end else file_size - 1

        # Ограничиваем диапазон, чтобы избежать выхода за границы файла
        end = min(end, file_size - 1)
        length = end - start + 1

        # Чтение и отправка нужного сегмента видео
        with open(file_path, 'rb') as f:
            f.seek(start)
            data = f.read(length)
            response = HttpResponse(data, status=206, content_type='video/mp4')
            response['Content-Range'] = f'bytes {start}-{end}/{file_size}'
            response['Accept-Ranges'] = 'bytes'
            response['Content-Length'] = str(length)
        return response

    # def product_details(request, product_id):
    #     """Отображает продукт по его ID"""
    #     product = Product.objects.get(id=product_id)
    #     context = {
    #         'product': product
    #     }
    #
    #     return render(request, template_name='catalog/product_info.html', context=context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    # fields = ['name', 'description', 'image', 'category', 'price', 'videos']
    template_name = 'catalog/add_products.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:success')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ['name', 'description', 'image', 'category', 'price', 'videos']
    template_name = 'catalog/add_products.html'
    success_url = reverse_lazy('catalog:main_page')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_form_class(self):
        user = self.request.user

        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm

        else:
            return ProductForm


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:main_page')
    context_object_name = 'product'

    def get_object(self, queryset=None):
        """
        Переопределяем метод get_object для проверки доступа.
        """
        product = super().get_object(queryset)
        user = self.request.user

        # Проверяем, является ли пользователь владельцем или имеет нужное разрешение
        if product.owner == user or user.has_perm('catalog.can_delete_product'):
            return product

        # Если пользователь не авторизован для удаления
        raise PermissionDenied("Вы не можете удалять этот продукт")





    # render(request, 'catalog/product_info.html', {'video_instance': video_instance})

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
