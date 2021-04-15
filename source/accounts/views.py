from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from webapp.forms import ProjectFormUpdateUsers
from webapp.models import Project
from .forms import MyUserCreationForm


# Create your views here.


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task:view')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/regis.html', context={'form': form})

