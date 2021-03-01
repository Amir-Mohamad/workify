from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    promote = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.author} wrote {self.title} at {self.created}'
