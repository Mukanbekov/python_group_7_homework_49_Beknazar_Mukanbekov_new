from django import forms

from webapp.models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name', 'description', 'status', 'type')


class TaskDeleteForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, label='Введите имя, чтобы удалить её')