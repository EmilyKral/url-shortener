from django import forms
from .models import URL


class URLForm(forms.ModelForm):
    original_url = forms.CharField()
    
    class Meta:
        model = URL
        fields = ['original_url']