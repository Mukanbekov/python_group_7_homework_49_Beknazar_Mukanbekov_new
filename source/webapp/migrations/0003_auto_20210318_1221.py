# Generated by Django 3.1.7 on 2021-03-18 12:21

from django.db import migrations, models
import webapp.ValidationError


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210315_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='description',
            field=models.TextField(max_length=2000, validators=[webapp.ValidationError.RegexValidator(['zzz', 'xxx', 'ccc', 'vvv'])], verbose_name='Поле'),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=100, validators=[webapp.ValidationError.MinLengthValidator(10)], verbose_name='Текст'),
        ),
    ]
