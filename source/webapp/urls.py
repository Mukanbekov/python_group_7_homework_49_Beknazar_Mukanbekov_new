"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import (
    IndexView,
    Detail,
    Create,
    Update,
    Delete,
    ListProject,
    ListProjectCreate,
    DetailProject,
    ProjectUpdateView,
    ProjectDeleteView,
)

app_name = 'task'

urlpatterns = [
    path('', IndexView.as_view(), name='view'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('<int:pk>/add/', Create.as_view(), name='create'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),

    path('project/', ListProject.as_view(), name='project_view'),
    path('project/<int:pk>/', DetailProject.as_view(), name='project_detail'),
    path('project/create/', ListProjectCreate.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
]