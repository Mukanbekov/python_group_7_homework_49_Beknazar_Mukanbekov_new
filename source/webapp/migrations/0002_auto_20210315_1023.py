# Generated by Django 3.1.7 on 2021-03-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип', 'verbose_name_plural': 'Типы'},
        ),
        migrations.RemoveField(
            model_name='list',
            name='type',
        ),
        migrations.AddField(
            model_name='list',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='lists', to='webapp.Type'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(max_length=200, verbose_name='Тип'),
        ),
        migrations.AlterModelTable(
            name='type',
            table='types',
        ),
    ]