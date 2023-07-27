from django import forms

from .models import Invigilator



class InvigilatorLoginForm(forms.ModelForm):

    class Meta:
        model = Invigilator
        fields = ['username', 'password']
