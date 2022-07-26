from django import forms
from .models import *

class upload_form(forms.ModelForm):
    class Meta:
        model=upload_img
        fields=['image_upload']