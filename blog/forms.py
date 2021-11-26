from django.forms import ModelForm
from django import forms
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class PostFilterForm(forms.Form):
    tag = forms.CharField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)