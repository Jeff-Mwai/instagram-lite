from django.shortcuts import render,redirect
from django.http  import HttpResponse, HttpResponseRedirect
from .models import Image, Profile, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404



# Create your views here.
@login_required(login_url="/accounts/login/")
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

def search_results(request):

    if 'person' in request.GET and request.GET["person"]:
        search_term = request.GET.get("person")
        searched_profile = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_profile": searched_profile})

    else:
        message = "You haven't searched for any profile"
        return render(request, 'search.html',{"message":message})

# def update_Profile(request):
#     if request.method == 'POST':
#         userForm = updateProfileForm(request.POST, instance=request.user)
#         profile_form = profileForm(
#             request.POST, request.FILES, instance=request.user)
#         if  profile_form.is_valid():
#             userForm.save()
#             profile_form.save()
#             return redirect('profile')
#     else:
#         profile_form = profileForm(instance=request.user)
#         user_form = UserUpdateForm(instance=request.user)
#         params = {
#             'user_form':user_form,
#             'profile_form': profile_form
#         }
#     return render(request, 'editprofile.html', params)


@login_required(login_url='/accounts/login/')
def comment(request,id):
    images = Image.objects.filter(id=id).all()
    comments = Comment.objects.filter(post=id).all()
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    image = get_object_or_404(Image, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = image
            comment.user = user_profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request,'comment.html',{"form":form,"images":images, "comments": comments})

