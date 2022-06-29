from django.conf import settings
from django.db import models


class Blog(models.Model):
    
    title = models.CharField(max_length=128, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    blogs = models.ManyToManyField("self", blank=True,symmetrical=False)
    blog_photo = models.ImageField(null = True , blank = True)


class Message(models.Model):
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_send = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    