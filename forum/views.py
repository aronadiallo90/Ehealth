from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.




def home(request):
    return render(request, 'forum/index.html')

@login_required
def forum(request):
    return render(request, 'forum/accueil.html')