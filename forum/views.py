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


@login_required
def blog_create(request):
    if request.method == 'POST':
        form  = BlogForm(request.POST)
        if form.is_valid :
            band = form.save()
        return redirect('forum', band.id)
        
    else :
        form = BlogForm()
    return render(request,'listings/band_create.html', {'form':form})
@login_required
def forum(request):
    blogs = Blog.objects.all()
     
    
    return render(request,'forum/accueil.html', {'blogs':blogs,})
