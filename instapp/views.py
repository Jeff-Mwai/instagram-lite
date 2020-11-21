from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Profile
from django.contrib.auth.models import User
from .forms import PostForm



# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    pass

def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            form.user = current_user
           
            form.save()
            
        return redirect('index')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})



