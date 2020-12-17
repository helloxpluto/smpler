from django import forms
from .models import Sample



class UploadForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = ('title', 'sound')
