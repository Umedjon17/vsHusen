from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    descriptions = models.TextField(verbose_name='Описание')
    created = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
