from django import forms
from .models import Profile
from django.forms.extras.widgets import SelectDateWidget

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'birth_date': SelectDateWidget(),
        }
