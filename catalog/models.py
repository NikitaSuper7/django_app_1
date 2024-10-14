from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', width_field=200, height_field=200, help_text='Изображение продукта')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Категория')
    category_description = models.TextField(verbose_name='Описание категории')

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
