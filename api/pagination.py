# Пагинация
from rest_framework.pagination import (
                LimitOffsetPagination,
                PageNumberPagination
                )

# Ограничение по 2 записи
class ContactLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

# Страница по 3 записи
class ContactPageNumberPagination(PageNumberPagination):
    page_size = 3