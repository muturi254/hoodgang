from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Profile, Business, Post
from django.contrib import messages
from .forms import ProfileForm, NeighbourhoodForm, PostForm, BusinessForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    current_user = request.user.profile
    post = Post.objects.filter(post_by__neighbourhood=current_user.neighbourhood)
    # print(post)
    
    return render(request, 'home.html', {'post':post})
@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
@transaction.atomic
def profile_edit(request, user_id):
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            # messages.success(request, _(
            #     'Your profile was successfully updated!'))
            return redirect('profile', user_id)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit-profile.html', {"profile_form": profile_form})


@login_required(login_url='/accounts/login/')
def new_hood(request):
    if request.method == 'POST':
        hood_form = NeighbourhoodForm(request.POST)
        if hood_form.is_valid():
            hood_form.save()
            return redirect('home')
    
    else:
        hood_form = NeighbourhoodForm()
    return render(request, 'hood.html', {'hood_form': hood_form})
@login_required(login_url="/accounts/login/")
def hood_post(request):
    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.post_by_id = current_user.id
            post_form.save()
            return redirect('home')

    else:
        post_form = PostForm()
    return render(request, 'newpost.html', {'post_form': post_form})

@login_required(login_url="/accounts/login/")
def new_bisuness(request):
    current_user = request.user
    if request.method == 'POST':
        biz_form = BusinessForm(request.POST)
        if biz_form.is_valid():
            form = biz_form.save(commit=False)
            form.business_owner = current_user
            biz_form.save()

            return redirect('home')
    else:
        biz_form = BusinessForm()
    return render(request, 'business.html', {'biz_form': biz_form})
