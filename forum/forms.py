from django import forms

from . import models



class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'blog_photo']

class MessageForm(forms.ModelForm):
    class Meta:   
        model = models.Message
        fields = ('content',) 