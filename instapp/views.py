from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm



# Create your views here.
def index(request):
    posts = Image.objects.all()
    return render(request, 'index.html',{"posts":posts})

def profile(request):
    return render(request, 'profile.html')

@login_required(login_url="/accounts/login/")
def new_post(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.user = current_user 
            image = form.cleaned_data.get('image')
            image_caption = form.cleaned_data.get('image_caption')
            post = Image(image = image,image_caption = image_caption,profile = user_profile)
            post.save_image() 
            # post.save()   
        return redirect('index')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})


# def new_post(request):
#     images = Image.objects.all()
#     users = User.objects.exclude(id=request.user.id)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user.profile
#             post.save()
#         return redirect('index')
#     else:
#         form = PostForm()
#     params = {
#         'images': images,
#         'form': form,
#         'users': users,

#     }
#     return render(request, 'new_post.html', params)

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    print(followers)
    return render(request, 'user_profile.html', params)

