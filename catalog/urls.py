from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", views.contact, name="contacts"),
    path("main_page/", views.main_page, name="main_page"),
    path("catalog/", views.catalog, name="catalog"),
    path("category/", views.category, name="category"),
    # path('pages/', views.pages, name='pages')
    path('index/', views.index, name='index'),
    path('category_list/', views.category_list, name='categories_lists'),
    path('product_info/<int:product_id>', views.product_details, name='product_details')
]
