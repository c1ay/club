from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):

    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name


class Article(models.Model):

    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    content = RichTextField()
    create_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
