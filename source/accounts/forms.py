from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import Profile
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput


class MyUserCreationForm(forms.ModelForm):
    email = forms.CharField(max_length=30, required=True)
    password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput, strip=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        if not cleaned_data.get('first_name') and not cleaned_data.get('last_name'):
            raise forms.ValidationError('First name or last name should be registered.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Форма редактирвоания данных профилья пользователя
    """
    class Meta:
        model = Profile
        exclude = ('user',)


class UserUpdateFrom(forms.ModelForm):
    """
    Форма редактирвоания данных пользователя
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')


class UserChangePasswordForm(forms.ModelForm):
    """
    Форма смены пароля
    """
    old_password = forms.CharField(required=True, label='Старый пароль', widget=PasswordInput)
    new_password = forms.CharField(required=True, label='Новый пароль', widget=PasswordInput)
    password_confirm = forms.CharField(required=True, label='Подтверждение пароля', widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password', 'password_confirm')

    def clean_password_confirm(self):
        """
        https://docs.djangoproject.com/en/3.2/ref/forms/validation/#form-and-field-validation
        В данном методе выполняется валидация подтверждения пароля (Проверяется, что
        новый пароль и подтверждение пароля совпадают).
        """
        new_password = self.cleaned_data.get('new_password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if new_password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return new_password

    def clean_old_password(self):
        """
        https://docs.djangoproject.com/en/3.2/ref/forms/validation/#form-and-field-validation
        В данном методе выполняется валидация старого пароля (Проверяем, что введённый старый
        пароль соответствует текущему пароль пользователя).
        """
        old_password = self.cleaned_data.get('old_password')

        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Пароль введён не верно')

        return old_password

    def save(self, commit=True):
        """
        При сохранении устанавливаем пароль используя метод пользователя set_password
        """
        user = self.instance
        user.set_password(self.cleaned_data.get('new_password'))
        if commit:
            user.save()
        return user