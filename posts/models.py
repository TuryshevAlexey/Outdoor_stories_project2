from django.db import models
from django.urls import reverse
from pkg_resources import require
from pytils.translit import slugify
from users.models import User
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        help_text='Название категории'
    )
    slug = models.SlugField(
        'Адрес для страницы c категорией',
        max_length=50,
        unique=True,
        blank=True,
        help_text=(
            'Укажите уникальный адрес для страницы задачи. Используйте только '
            'латиницу, цифры, дефисы и знаки подчёркивания'
        )
    )
    description = models.TextField(
        'Описание',
        help_text='Опишите категорию'
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:100]
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    text = HTMLField(
        'Текст',
        help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
        help_text='Автор поста'
    )
    category = models.ForeignKey(
        Category,
        related_name='posts',
        # blank=True,
        # null=True,
        on_delete=models.CASCADE,
        help_text='Выберите категорию',
        verbose_name='Категория',
    )
    photo = models.ImageField(
        'Изображение',
        upload_to="images/%Y/%m/%d/",
        help_text='Добавьте изображение к посту',
        # null=True,
        # blank=True,
    )
    is_published = models.BooleanField(
        blank=False,
        verbose_name='Публикация',
        default=False,
        help_text='Опубликовать или оставить в черновике?',
        )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(
        User,
        verbose_name='Автор поста',
        related_name='comment',
        on_delete=models.CASCADE
    )
