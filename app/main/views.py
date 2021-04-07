import requests

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from .serializers import ItemListSerializer, ItemSerializer
from app.main.models import Item
from app.utils.cache import cache_data


class ItemsCreateView(APIView):
    """Создание объектов"""

    def post(self, request):
        serializer = ItemListSerializer(data=request.data, child=ItemSerializer())
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


class ItemsView(GenericAPIView):
    """Отдача всех объектов из базы"""

    serializer_class = ItemSerializer
    queryset = Item.objects

    def get(self, request):
        items = self.get_serializer(self.queryset, many=True).data
        return Response(
            items,
            status=status.HTTP_200_OK
        )


class ItemUpdateView(GenericAPIView):
    """Обновление отдельного объекта"""

    serializer_class = ItemSerializer
    queryset = Item

    def patch(self, request, item_id):
        item = get_object_or_404(self.queryset, pk=item_id)
        updated_item = self.get_serializer(item, data=request.data).load_and_save()

        return Response(
                ItemSerializer(updated_item).data,
                status=status.HTTP_200_OK
        )


class ProxyView(APIView):
    """Проксирование API, который указывается в атрибуте upstream"""

    upstream = 'https://kats1.skbkontur.ru/api_test/test.json'

    def get(self, request):
        proxy_value = cache_data(data=requests.get(self.upstream).text, cache_name='proxy_value')
        return Response(
            data=proxy_value.strip(),
            status=status.HTTP_200_OK
        )
