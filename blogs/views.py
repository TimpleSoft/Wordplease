# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import View
from blogs.forms import PostForm
from models import Post
from settings import MAX_POSTS_HOME, MAX_POSTS_BLOG_DETAIL
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
        return render(request, 'blogs/home.html', context)




class BlogsListView(View):

    def get(self, request):
        """
        Devuelve una lista de los usuarios, y por lo tanto blogs, que hay registrados
        """
        users = User.objects.all().order_by('first_name')
        context = {
            'users_list': users
        }
        return render(request, 'blogs/blogs_list.html', context)



class BlogDetailView(View):

    def get(self, request, username):
        """
        Carga el detalle de un blog, los post del usuario pasado por parámetro.
        Por orden de publicación descendente
        """

        #obtenemos el usuario
        possible_user = User.objects.filter(username=username)
        user = possible_user[0] if len(possible_user) > 0 else None

        if user is not None:
            # obtenemos sus posts y los añadimos al contexto
            user_posts = Post.objects.filter(owner=user).order_by('-publication_date')
            context = {
                'blog_user': user,
                'posts_list': user_posts[:MAX_POSTS_BLOG_DETAIL]
            }
            return render(request, 'blogs/blog_detail.html', context)

        else:
            # devolvemos not found
            return HttpResponseNotFound('No hay ningún blog para el usuario indicado.')




class PostDetailView (View):

    def get(self, request, username, pk):
        """
        Carga la página detalle de un post del usuario pasado por parámetro
        """

        #obtenemos el usuario
        possible_user = User.objects.filter(username=username)
        user = possible_user[0] if len(possible_user) > 0 else None

        if user is not None:

            #obtenemos el post
            possible_post = Post.objects.filter(pk=pk, owner=user).select_related('owner')
            post = possible_post[0] if len(possible_post) > 0 else None

            if post is not None:
                # cargamos la plantilla de detalle
                context = {
                    'post': post
                }
                return render(request, 'blogs/post_detail.html', context)

            else:
                # devolvemos not found
                return HttpResponseNotFound('No existe el post o no pertenece al blog seleccionado.')

        else:

            # devolvemos not found
            return HttpResponseNotFound('No existe el blog.')




class CreatePostView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Muestra formulario para añadir un post
        """
        form = PostForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'blogs/new_post.html', context)


    @method_decorator(login_required())
    def post(self, request):
        """
        Crea un post a partir de la información POST
        """
        success_message = ''
        post_with_owner = Post()
        post_with_owner.owner = request.user # aquí asignamos al usuario como propietario del post
        form = PostForm(request.POST, instance=post_with_owner)

        if form.is_valid():

            new_post = form.save()
            form = PostForm() # reiniciamos el form
            success_message = 'Post almacenado con éxito! '
            success_message += '<a href="{0}">'.format(
                reverse('post_detail', args=[request.user.username, new_post.pk])
            )
            success_message += 'Ver post'
            success_message += '</a>'

            context = {
                'form': form,
                'success_message': success_message
            }
            return render(request, 'blogs/new_post.html', context)


