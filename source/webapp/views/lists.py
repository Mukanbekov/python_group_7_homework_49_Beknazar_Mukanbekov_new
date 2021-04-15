from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.models import List, Project
from webapp.forms import ListForm, SearchForm, ProjectFormUpdateUsers


class IndexView(ListView):
    template_name = 'lists/index.html'
    model = List
    context_object_name = 'lists'
    ordering = ('name', '-created_at')
    paginate_by = 8
    paginate_orphans = 0

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super().get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class Detail(DetailView):
    template_name = 'lists/view.html'
    model = List


class Create(PermissionRequiredMixin, CreateView):
    model = Project
    template_name = 'lists/create.html'
    form_class = ListForm
    permission_required = 'webapp.add_list'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        list = form.save(commit=False)
        list.project = project
        list.save()
        form.save_m2m()
        return redirect('task:detail', pk=list.pk)

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()


class Update(PermissionRequiredMixin, UpdateView):
    form_class = ListForm
    model = List
    template_name = 'lists/update.html'
    context_object_name = 'list'
    permission_required = 'webapp.change_list'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('task:detail', kwargs={'pk': self.kwargs.get('pk')})

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.user.all()


class Delete(PermissionRequiredMixin, DeleteView):
    model = List
    template_name = 'lists/delete.html'
    context_object_name = 'list'
    success_url = reverse_lazy('task:view')
    permission_required = 'webapp.delete_list'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        return super().dispatch(request, *args, **kwargs)

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.user.all()
