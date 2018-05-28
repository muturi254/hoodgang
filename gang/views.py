from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Profile, Business
# Create your views here.
def index(request):
    profile = Profile.objects.filter(user=request.user)
    print(Profile._meta.get_fields())
    return render(request, 'index.html')

def home(request):
    
    return render(request, 'home.html')
@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
@transaction.atomic
def profile_edit(request, user_id):
    # if request.method == 'POST':
    #     profile_form = ProfileForm(
    #         request.POST, request.FILES, instance=request.user.profile)
    #     if profile_form.is_valid():
    #         profile_form.save()
    #         # messages.success(request, _(
    #         #     'Your profile was successfully updated!'))
    #         return redirect('profile', user_id)
    #     else:
    #         messages.error(request, ('Please correct the error below.'))
    # else:
    #     profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit-profile.html')
