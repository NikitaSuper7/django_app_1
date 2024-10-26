from django.db import models


# Create your models here.
class BlogPostsModel(models.Model):
    """Модель для блога"""
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="введите заголовок статьи")
    text = models.TextField(verbose_name="Содержание", help_text="Введите содержание статьи")
    image = models.ImageField(
        upload_to="media/media_blog/photos/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",

    )
    created_at = models.DateField(verbose_name="Дата создания", help_text='Введите дату создания',
                                  auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата изменения", help_text='Введите дату изменения',
                                  auto_now=True)
    is_publicated = models.BooleanField(verbose_name='Признак публикации', default=False)
    views_counter = models.PositiveIntegerField(verbose_name="счетчик просмотров", default=0)

    def __str__(self):
        return f"{self.title}, Опубликовано - {self.is_publicated}"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
