from django.contrib import admin

# Register your models here.
from  forum.models import Message,Blog

admin.site.register(Message)
admin.site.register(Blog)