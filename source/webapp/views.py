from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import TemplateView, View, ListView

from webapp.models import List
from webapp.forms import ListForm, TaskDeleteForm, SearchForm


class IndexView(ListView):
    template_name = 'index.html'
    model = List
    context_object_name = 'lists'
    ordering = ('name', '-created_at')
    paginate_by = 10
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


class DetailView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['list'] = get_object_or_404(List, id=kwargs.get('id'))
        return super().get_context_data(**kwargs)


class IndexRedirectView(View):
    def get(self, request, **kwargs):
        form = ListForm()
        return render(request, 'task_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = ListForm(data=request.POST)
        if form.is_valid():
            type = form.cleaned_data.get('type')
            task = List.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status')
            )
            task.type.set(type)
            return redirect('index_view')
        return render(request, 'task_create.html', context={'form': form})


class UpdateView(View):
    def get(self, request, **kwargs):
        task = get_object_or_404(List, id=kwargs.get('id'))
        form = ListForm(initial={
            'name': task.name,
            'description': task.description,
            'status': task.status,
            'type': task.type.all()
        })
        return render(request, 'task_update.html', context={'form': form, 'list': task})

    def post(self, request, **kwargs):
        task = get_object_or_404(List, id=kwargs.get('id'))
        form = ListForm(data=request.POST)
        if form.is_valid():
            task.name = form.cleaned_data.get("name")
            task.description = form.cleaned_data.get("description")
            task.status = form.cleaned_data.get("status")
            # task.type = form.cleaned_data.get("type")
            task.save()
            task.type.set(form.cleaned_data.get("type"))
            return redirect('index_view')
        return render(request, 'task_update.html', context={'form': form, 'list': task})


class DeleteView(View):
    def get(self, request, **kwargs):
        task = get_object_or_404(List, id=kwargs.get('id'))
        form = TaskDeleteForm()
        return render(request, 'task_delete.html', context={'list': task, 'form': form})

    def post(self, request, **kwargs):
        task = get_object_or_404(List, id=kwargs.get('id'))
        form = TaskDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['name'] != task.name:
                form.errors['name'] = ['Названия не совпадают']
                return render(request, 'task_delete.html', context={'list': task, 'form': form})

            task.delete()
            return redirect('index_view')
        return render(request, 'task_delete.html', context={'list': task, 'form': form})