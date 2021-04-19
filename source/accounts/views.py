from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator

# from django.urls import reverse_lazy
# from django.views.generic import UpdateView
#
# from webapp.forms import ProjectFormUpdateUsers
# from webapp.models import Project
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


class UserDetailView(PermissionRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'registration/user_detail.html'
    permission_required = ('accounts.You_have_no_rights',)

    context_object_name = 'user_obj'
    paginate_related_by = 3
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        project = self.get_object().users.all()
        paginator = Paginator(project, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['projects'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


