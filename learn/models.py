from django.db import models
from accounts.models import User


class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    video = models.FileField() # I DONT KNOW 
    is_active = models.BooleanField(default=True)
    is_special = models.BooleanField(default=True)

    def __str__(self):
        return self.title
