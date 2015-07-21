# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from models import Post
from settings import MAX_POSTS_HOME
from django.http import HttpResponseNotFound


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


class DetailView (View):

    def get(self, request, pk):
        """
        Carga la página detalle de un post
        """

        #obtenemos el post
        possible_post = Post.objects.filter(pk=pk).select_related('owner')
        post = possible_post[0] if len(possible_post) > 0 else None

        if post is not None:
            # cargamos la plantilla de detalle
            context = {
                'post': post
            }
            return render(request, 'posts/post_detail.html', context)

        else:
            # devolvemos not found
            return HttpResponseNotFound('No existe el post.')