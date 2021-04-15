from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import reverse, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.forms import ProjectForm, ProjectFormUpdate, ProjectFormUpdateUsers
from webapp.models import Project


class ListProject(ListView):
    template_name = 'projects/index.html'
    model = Project
    context_object_name = 'projects'
    ordering = 'name'
    paginate_by = 4
    paginate_orphans = 0


class DetailProject(DetailView):
    template_name = 'projects/view.html'
    model = Project


class ListProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'projects/create.html'
    form_class = ProjectForm
    permission_required = 'webapp.add_project'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('task:project_detail', kwargs={"pk": self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/update.html'
    form_class = ProjectFormUpdate
    context_object_name = 'project'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('task:project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'projects/delete.html'
    model = Project
    context_key = 'project'
    success_url = reverse_lazy('task:project_view')
    permission_required = 'webapp.delete_project'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        return super().dispatch(request, *args, **kwargs)


class UserUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/UsersUpdate.html'
    permission_required = 'webapp.update_delete_user'
    form_class = ProjectFormUpdateUsers

    def get_success_url(self):
        return redirect('task:project_view')

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()
