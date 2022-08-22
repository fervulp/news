from dataclasses import fields
from django.contrib import admin
from .models import Category, News
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.
  

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    search_fields = ('title', 'content')
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    list_display_links = ('title', 'id')
    list_editable = ('is_published','category')
    list_filter = ('category', 'is_published')

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title')
    list_display_links = ('title', 'id')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)



