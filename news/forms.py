import re
from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .admin import NewsAdminForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget = forms.TextInput(attrs={'class': "form-control"}) )
    password = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={'class': "form-control"}) )
    
# class TestForm(forms.Form):
#     content = forms.CharField(widget=CKEditorWidget, label='')


class NewsForm(forms.ModelForm):
    # content = forms.CharField(max_length=10000, label='Текст', widget=forms.Textarea(attrs={'class': "form-control", 'row': 5}), required=False)
    # content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'content': CKEditorUploadingWidget(),
            'category': forms.Select(attrs={'class': "form-control"}) 
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget = forms.TextInput(attrs={'class': "form-control"}) )
    password1 = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={'class': "form-control"}) )
    password2 = forms.CharField(label="Подтверждение пароля", widget = forms.PasswordInput(attrs={'class': "form-control"}) )
    email = forms.EmailField(label='E-mail', widget = forms.EmailInput(attrs={'class': "form-control"}) )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', 
#     widget=forms.TextInput(attrs={'class': "form-control"}) )

#     content = forms.CharField(max_length=10000, label='Текст', 
#     widget=forms.Textarea(attrs={'class': "form-control", 'row': 5}), required=False)

#     is_published = forms.BooleanField(label='Опубликовать', initial=True)

#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='', widget=forms.Select(attrs={'class': "form-control"}))

#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if re.match(r'\d', title):
#             raise ValidationError('Название не должно начинаться с цифры')
#         return title