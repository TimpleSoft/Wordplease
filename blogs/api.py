# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView
from blogs.models import Post
from blogs.serializers import PostSerializer, PostListSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from permissions import PostPermission
from django.core.urlresolvers import reverse
import datetime



class PostQueryset(object):


    def get_posts_queryset(self, request):

        # obtenemos el usuario
        possible_user = User.objects.filter(username=self.kwargs.get('username'))
        user = possible_user[0] if len(possible_user) > 0 else None

        if user is not None:
            if request.user.is_superuser or user == request.user:  # si es adminsitrador o el propietario del blog
                posts = Post.objects.filter(owner=user).order_by('-publication_date')
            else:
                # los post publicados ya, del usuario
                posts = Post.objects.filter(publication_date__lt=datetime.datetime.now(), owner=user).order_by('-publication_date')
            return posts

        else:
            # si no existe el usuario devolvemos un queryset vacío
            return possible_user




class PostViewSet(PostQueryset, ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, PostPermission,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'abstract', 'body')
    ordering_fields = ('title', 'publication_date')


    def get_queryset(self):
        return self.get_posts_queryset(self.request)


    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de la nueva foto
        al usuario autenticado
        """
        serializer.save(owner=self.request.user)


class APIBlogsListView(APIView):


    def get(self, request):
        """
        Devuelve una lista de los usuarios, y por lo tanto blogs, que hay registrados y sus urls
        """
        users = User.objects.all().order_by('first_name')
        # no usamos serializers, ya que los datos los estamos "inventando"
        response = []

        for user in users:
            dict = {
                'blog': 'El blog de ' + user.first_name + ' ' + user.last_name,
                'url': request.build_absolute_uri(reverse('api_blog_detail', args=[])) + user.username
            }
            response.append(dict)

        return Response(response)