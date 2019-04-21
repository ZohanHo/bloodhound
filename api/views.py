from django.db.models import Q

# Фильтр и сортировка
from rest_framework.filters import (
                SearchFilter,
                OrderingFilter
                )


# Права доступа
from rest_framework.permissions import (
                        AllowAny,  # разрешить любому
                        IsAuthenticated, # разрешить только авторизированым
                        IsAdminUser, # Только Админ
                        IsAuthenticatedOrReadOnly # Разрешить авторизированым только для чтения
                        )
# Можем создать права сами и импортировать с permission
from .permission import IsOwnerOrReadOnly

# Импортируеи зфпштфешщты
from .pagination import ContactLimitOffsetPagination, ContactPageNumberPagination

# Retrieve - извлечь
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    )
from base.models import Contact
from REST.serializers import ContactSerializer, ContactCreateSerializer
from django.contrib.auth.models import User

# List and search
class ContactListApiView(ListAPIView):
    #queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    #Добавив 2 поля лрганизуем поиск  по GET запросу ?Serch=, и через ?ordering= сортировка
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "phone", "slug", "id"]

    # Пагинация
    #pagination_class = LimitOffsetPagination  # ?limit=2     лимит на 2 записи  &offset=1   отобразит 2,3 запись
    #pagination_class = PageNumberPagination

    # Class импортированый с файла paginations
    pagination_class = ContactPageNumberPagination #ContactLimitOffsetPagination


    #search
    def get_queryset(self, *args, **kwargs):
        queryset_list = Contact.objects.all()
        # Самописный поисковик
        query = self.request.GET.get("s")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__iexact=query) |
                Q(phone__icontains=query) |
                Q(slug__icontains=query) |
                Q(pk__icontains=query)
            ).distinct()
        return queryset_list

# Detail
class DetailListApiView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # lookup_field - по какому полю будет поиск (для выботв в urls конкретного обьекта), по умолчанию pk
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Не разобрался
    #lookup_url_kwarg = ""

# Delete
class ContactDeleteApiView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # lookup_field - по какому полю будет поиск, по умолчанию pk
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


# Update
#  UpdateAPIView - обновить данные, поля пустые
#  UpdateAPIViewRetrieveUpdateAPIView - обновить данные, поля заполнены
class ContactUpdateApiView(RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # lookup_field - по какому полю будет поиск в urls, по умолчанию pk
    lookup_field = 'pk'#Поля которые будут указаны по умолчанию
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)

# Create
class ContactCreateApiView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
    # lookup_field - по какому полю будет поиск в urls, по умолчанию pk
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    #Поля которые будут указаны по умолчанию
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

