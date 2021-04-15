from django.db import models


from webapp.ValidationError import MinLengthValidator, RegexValidator

regex = ['zzz', 'xxx', 'ccc', 'vvv']
# Create your models here.


class Status(models.Model):
    status = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return "{}. {}".format(self.id, self.status)


class Type(models.Model):
    type = models.CharField(max_length=200, null=False, blank=False, verbose_name='Тип')

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.type


class List(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Текст',
                            validators=(MinLengthValidator(5),))
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Поле',
                                   validators=(RegexValidator(regex),))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.ForeignKey('webapp.Status', related_name='lists', on_delete=models.CASCADE)
    type = models.ManyToManyField('webapp.Type', related_name='lists', blank=True)
    project = models.ForeignKey('webapp.Project', related_name='Project', on_delete=models.CASCADE)

    class Meta:
        db_table = 'lists'
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return "{}. {}".format(self.id, self.name, self.description)


class Project(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Текст',
                            validators=(MinLengthValidator(5),))
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Поле',
                                   validators=(RegexValidator(regex),))
    created_at = models.DateField(blank=False, null=False, verbose_name='Время создания')
    updated_at = models.DateField(verbose_name='Время окончания')
    user = models.ManyToManyField('auth.User', blank=True, verbose_name='user', related_name='users')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        permissions = [
            ('update_delete_user', 'редактировать пользователя')
        ]

    def __str__(self):
        return "{}. {}".format(self.id, self.name, self.description)
