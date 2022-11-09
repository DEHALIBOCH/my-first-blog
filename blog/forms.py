from django import forms
from .models import Post
from django.forms import ModelForm, TextInput, Textarea, ImageField


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }

