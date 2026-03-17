from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PostModel(models.Model):
    id =models.AutoField(primary_key=True)
    title =models.CharField(max_length=200)
    body =models.TextField()
    image = models.ImageField(default=None,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    category = models.ManyToManyField(CategoryModel)
    created_at =models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.content