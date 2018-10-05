from .models import *
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['poster', 'likes', 'imagecomments',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


