from django import forms
from .models import Blog , CommentBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title' , 'body' , 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = ['comment']