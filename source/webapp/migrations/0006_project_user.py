# Generated by Django 3.1.7 on 2021-04-14 12:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0005_list_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]