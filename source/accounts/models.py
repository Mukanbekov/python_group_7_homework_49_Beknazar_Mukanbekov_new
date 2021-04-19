from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    git = models.URLField(max_length=70, blank=True, null=True, verbose_name='Ссылка')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Поле')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions =[
            ( 'You_have_no_rights','Проверка профиля')
        ]