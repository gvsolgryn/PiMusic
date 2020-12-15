from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from .models import *
 
class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
 
        fields = ['comment_textfield']
        widgets = {
            'comment_user': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'cols': 20}),
            'comment_textfield': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
        }
        labels = {
            'comment_user': '닉네임',
            'comment_textfield': '내용',
        }