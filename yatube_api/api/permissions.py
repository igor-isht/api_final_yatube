from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


# Пермишен для подписок
class GetAndPost(permissions.BasePermission):
    message = 'Запрещено'

    def has_object_permission(self, request, view, obj):
        return request.method == ('GET' or 'POST')
