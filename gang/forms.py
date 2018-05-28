from django import forms
from .models import Profile, Neighbourhood, Post, Business
from django.forms.extras.widgets import SelectDateWidget

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'birth_date': SelectDateWidget(),
        }

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['hood_admin']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['post_by']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['business_owner']
