from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import reverse, get_object_or_404

from webapp.forms import ProjectForm, ProjectFormUpdate
from webapp.models import Project


class ListProject(ListView):
    template_name = 'projects/index.html'
    model = Project
    context_object_name = 'projects'
    ordering = 'name'
    paginate_by = 2
    paginate_orphans = 0


class DetailProject(DetailView):
    template_name = 'projects/view.html'
    model = Project


class ListProjectCreate(CreateView):
    template_name = 'projects/create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_detail', kwargs={"pk": self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/update.html'
    form_class = ProjectFormUpdate
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'projects/delete.html'
    model = Project
    context_key = 'project'
    success_url = reverse_lazy('project_view')
