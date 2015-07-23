# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Siempre podemos hacer GET, se filtra con el queryset
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (PUT o DELETE)
        sobre el object obj
        """
        if request.method == "GET":
            return True
        # si es superadmin, o el usuario autenticado intenta
        # hacer PUT o DELETE sobre su mismo perfil
        return request.user.is_superuser or request.user == obj.owner
