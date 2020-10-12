from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')


    def __str__(self):
         return self.title



    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
    #

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

