from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from forum.forms import *
from forum.models import *
# Create your views here.




def home(request):
    return render(request, 'forum/index.html')

# @login_required
# def forum(request):
#     return render(request, 'forum/accueil.html')




# @login_required
# def forum(request):
#     blogs = Blog.objects.all()
     
    
    return render(request,'forum/accueil.html', {'blogs':blogs,})

@login_required
def forum(request):
    blogs = Blog.objects.all()


    form = BlogForm()
    form1 = MessageForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)
        form1 = MessageForm(request.POST)
        if form.is_valid():
            photo = form.save(commit= False)
            photo.author = request.user
            photo.save()
        if form1.is_valid():
            msg = form.save(commit= False)
            msg.author = request.user
            msg.blog = form1.cleaned_data['blog']
            msg.save()

   
            
    return render(request,'forum/accueil.html', {'form':form,'blogs':blogs,'form1':form1})


