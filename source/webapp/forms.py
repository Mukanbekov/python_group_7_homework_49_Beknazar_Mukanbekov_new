from django import forms

from webapp.models import List, Project


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name', 'description', 'status', 'type')


class TaskDeleteForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, label='Введите имя, чтобы удалить её')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'created_at', 'updated_at')


class ProjectFormUpdate(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'updated_at')


class ProjectFormUpdateUsers(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('user',)
        widgets = {
            'user': forms.CheckboxSelectMultiple()
        }


