from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from article.models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # fields = ('name', 'categories', 'content', 'create_time')
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # fields = ('name', 'create_time')

    class Meta:
        model = Category
