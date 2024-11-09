from django.urls import path
from . import views
from blog.apps import BlogConfig
from django.conf import settings
from django.conf.urls.static import static

app_name = BlogConfig.name

urlpatterns = [
    path("articles/", views.BlogLIstView.as_view(), name='articles_list'),
    path("articles/new/", views.BlogCreateView.as_view(), name='article_form'),
    path("articles/<int:pk>/", views.BlogDetailView.as_view(), name='article_detail'),
    path("articles/update/<int:pk>/", views.BlogUpdateView.as_view(), name="article_update"),
    path("article/delete/<int:pk>/", views.BlogDeleteView.as_view(), name="article_delete")

    # path("contacts/", views.ContactsTemplateView.as_view(), name="contacts"),
    # path("main_page/", views.MainView.as_view(), name="main_page"),
    # path("catalog/", views.CatalogView.as_view(), name="catalog"),
    # path("category/", views.CategoryView.as_view(), name="category"),
    # path("success/", views.SuccesTemplateView.as_view(), name='success'),
    # # path('pages/', views.pages, name='pages')
    # # path('category_list/', views.category_list, name='categories_lists'),
    # path('product_info/<int:pk>', views.ProductDetailView.as_view(), name='product_details'),
    # path('add_products/', views.ProductCreateView.as_view(), name='add_products'),
    # path('success/', views.success, name='success')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)