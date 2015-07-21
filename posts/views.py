# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from models import Post
from settings import MAX_POSTS_HOME

class HomeView(View):

    def get(self, request):
        """
        Función que devuelve el home de la página
        """
        posts = Post.objects.all().order_by('-publication_date')
        context = {
            'posts_list': posts[:MAX_POSTS_HOME]
        }
        return render(request, 'posts/home.html', context)