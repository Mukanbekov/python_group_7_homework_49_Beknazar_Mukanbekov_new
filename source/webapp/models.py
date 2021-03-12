from django.db import models

# Create your models here.


class Status(models.Model):
    status = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return "{}. {}".format(self.id, self.status)


class Type(models.Model):
    type = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return "{}. {}".format(self.id, self.type)


class List(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Текст')
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name='Поле')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.ForeignKey('webapp.Status', related_name='lists', on_delete=models.CASCADE)
    type = models.ForeignKey('webapp.Type', related_name='lists', on_delete=models.CASCADE)

    class Meta:
        db_table = 'lists'
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return "{}. {}".format(self.id, self.name, self.description)


