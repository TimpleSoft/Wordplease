# -*- coding: utf-8 -*-
from django import forms
from models import Post

class PostForm (forms.ModelForm):

    """
    Formulario para el modelo Post
    """
    class Meta:
        model = Post
        exclude = ['owner']
