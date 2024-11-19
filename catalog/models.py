from django.db import models
from users.models import CustomUser


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name="Категория", help_text='Введите название категории')
    category_description = models.TextField(verbose_name="Описание категории", help_text='Введите описание категории')

    def __str__(self):
        return f"{self.category_name} - {self.category_description}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="media/photos",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",

    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        max_length=100,
        verbose_name="Категория",
        blank=True,
        null=True,
        related_name="Products",
        help_text='Выберите категорию продукта'
    )
    price = models.FloatField(verbose_name="Цена", help_text='Введите стоимость продукта')
    created_at = models.DateField(verbose_name="Дата создания", help_text='Введите дату создания продукта',
                                  auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата изменения", help_text='Введите дату изменения продукта',
                                  auto_now=True)
    videos = models.FileField(upload_to='media/videos', verbose_name="Видео", null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        max_length=100,
        verbose_name='Владелец',
        blank=True,
        null=True,
        related_name='Users',
        help_text='Выберите владельца продукта'
    )

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name", "price"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]

# Пример моделей
# class Student(models.Model):
#     """Примпер таблицы в БД"""
#     first_name = models.CharField(max_length=150, verbose_name='Name')
#     last_name = models.CharField(max_length=150, verbose_name='Surname', unique=True)
#
#     age = models.IntegerField(help_text='Введите возраст студента')
#     is_active = models.BooleanField()
#     description = models.TextField()
#     created_at = models.DateTimeField()
#     image = models.ImageField(upload_to='photos/', verbose_name='Фотография') # Нужна библиотека Pill
#
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag)
#
#     STATUS_CHOICES = [
#         ('draft', 'Draft'), # (запись в БД, отображение для пользователя)
#         ('published', 'Published'),
#     ]
#
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#     class Meta:
#         """Используется для добавления мета-данных"""
#         # отображаемые имена модели в ед. и мн. числе
#         verbose_name = 'студент'
#         verbose_name_plural = 'студенты'
#         # Порядок сортировки
#         ordering = ['last_name']
#         # Имя таблицы для нашей модели
#         db_table = 'custom_table_name'
