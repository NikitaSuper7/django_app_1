from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', views.contact, name='contacts'),
    path('main_page/', views.main_page, name='main_page'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/', views.category, name='category'),
]