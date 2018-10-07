from .models import *
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['poster', 'likes', 'imagecomments',]


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []
        # fields = [ 'profilepic','bio', 'email', 'contact']

