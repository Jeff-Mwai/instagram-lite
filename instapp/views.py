from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Profile
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    pass

def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

