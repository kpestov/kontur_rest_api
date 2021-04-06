from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ItemListSerializer, ItemSerializer


class ItemsCreateView(APIView):
    """View на создание объектов"""

    def post(self, request):
        serializer = ItemListSerializer(data=request.data, child=ItemSerializer())
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(
            {'items': ItemSerializer(serializer.data, many=True).data},
            status=status.HTTP_201_CREATED
        )
