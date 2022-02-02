from django import forms
from .models import URL


class URLForm(forms.ModelForm):
    original_url = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "http://my-url.co.uk"}))

    class Meta:
        model = URL
        fields = ['original_url']
