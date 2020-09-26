from django import forms

from .models import Bar_code, Upload_Img, Upload_Code, Upload, Review
from django.forms import ClearableFileInput

class PostForm(forms.ModelForm):

    class Meta:
        model = Bar_code
        fields = ('code', 'name', 'charge', 'image',)

class UploadForm_Img(forms.ModelForm):
    
    class Meta:
        model = Upload_Img
        fields = ( 'image', )

class UploadForm_Code(forms.ModelForm):
    
    class Meta:
        model = Upload_Code
        fields = ( 'title', )


class Multi_Upload(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review_text']