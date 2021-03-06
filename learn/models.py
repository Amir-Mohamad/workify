from django.db import models
from accounts.models import User


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube = models.CharField(max_length=500)
    aparat = models.CharField(max_length=500)

    def __str__(self):
        return 
        
class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    videos = models.ForeignKey(Video, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=500)
    cover = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.IntegerField() # I dont now the parameters
    is_active = models.BooleanField(default=True)
    is_special = models.BooleanField(default=True)


    def __str__(self):
        return self.title
