from django import forms

from forum.models import *



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class MessageForm(forms.ModelForm):
    class Meta:   
        model = Message
        fields = '__all__'