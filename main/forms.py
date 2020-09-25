from django import forms

from .models import Bar_code, Img

class PostForm(forms.ModelForm):

    class Meta:
        model = Bar_code
        fields = ('code', 'name', 'charge',)

class UploadForm(forms.ModelForm):
    
    class Meta:
        model = Img
        fields = ( 'title','image', )