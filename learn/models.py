from django.db import models
from accounts.models import User


class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    cover = models.ImageField()
    youtube = models.CharField(max_length=500) # Youtube
    aparat = models.CharField(max_length=500) # Aparat
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.IntegerField() # I dont now the parameters
    is_active = models.BooleanField(default=True)
    is_special = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    youtube = models.CharField(max_length=500)
    aparat = models.CharField(max_length=500)

    def __str__(self):
        return 