from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    """Рендерит главную страницу"""
    return render(request, template_name='catalog/main_page.html')

def catalog(request):
    """Рендерит страницу каталога"""
    return render(request, template_name='catalog/catalog.html')

def category(request):
    """Рендерит страницу категорий"""
    return render(request, template_name='catalog/category_page.html')



def contact(request):
    """Пример контроллера, обрабатывающий POST-запрос!"""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        return HttpResponse(f"Спасибо {name.title()}, вы успешно зарегестрированы с почтой -\n'{email}'.")
    # Чтобы приложение не падало в ошибку, возвращаем рендер нашего шаблона.
    return render(request, "catalog/contacts.html")