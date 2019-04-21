""""""
"""
Можем описать свои разрешения доступа к CRUD
"""
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = "Вы не можете редактировать запись, так как Вы ее не создавали"
    my_save_method = ['PUT', 'GET']

    def has_permission(self, request, view):
        """Методы должны возвращаться, True если запросу должен быть предоставлен доступ,
        и в False противном случае."""

        # Проверяем каким методом сделан запрос, и сравниваем с прописаным нами
        if request.method in  self.my_save_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Проверяем является операция чтения или запись
        if request.method in SAFE_METHODS: # SAFE_METHODS - кортеж, содержащим 'GET', 'OPTIONS'и 'HEAD'
            return True

        # (True - если user что создал записсь тоже же что сейчас залогинился)
        return obj.user == request.user