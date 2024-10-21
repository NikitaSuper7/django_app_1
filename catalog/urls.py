from django.urls import path
from . import views
from catalog.apps import CatalogConfig
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", views.contact, name="contacts"),
    path("main_page/", views.main_page, name="main_page"),
    path("catalog/", views.catalog, name="catalog"),
    path("category/", views.category, name="category"),
    # path('pages/', views.pages, name='pages')
    path('category_list/', views.category_list, name='categories_lists'),
    path('product_info/<int:product_id>', views.product_details, name='product_details'),
    path('add_products/', views.add_products, name='add_products'),
    # path('success/', views.success, name='success')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
