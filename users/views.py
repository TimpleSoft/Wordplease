from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View


class BlogsListView(View):

    def get(self, request):
        """
        Devuelve una lista de los usuarios, y por lo tanto blogs, que hay registrados
        """
        users = User.objects.all().order_by('first_name')
        context = {
            'users_list': users
        }
        return render(request, 'users/blogs_list.html', context)