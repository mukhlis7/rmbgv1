# forms.py
from django import forms
from .models import *


class ImgProcForm(forms.ModelForm):
    class Meta:
        model = ImgToProc
        fields = ['Image_To_Process']
