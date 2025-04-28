from django import forms
from fileupload.models import RegularFile


class RegularFileForm(forms.Form):
    file_name = forms.CharField(max_length=255)
    file = forms.FileField()
    image = forms.ImageField()
    
    class Meta:
        model = RegularFile
        fields = ["file_name","file","image"]