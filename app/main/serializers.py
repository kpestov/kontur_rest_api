from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import ValidationError

from app.main import base_serializers
from app.main.models import Item


class ItemListSerializer(serializers.ListSerializer):
    """Сериализатор списка объектов"""

    @staticmethod
    def _bulk_create_items(validated_items):
        """Метод отвечает за массовую вставку объектов в базу"""

        return Item.objects.bulk_create([
            Item(value=validated_item_data.get('value'))
            for validated_item_data in validated_items
        ])

    def validate(self, validated_data):
        """Валидирует входные данные от клиента"""

        duplicates = Item.objects.filter(value__in=[item.get('value') for item in validated_data])
        if duplicates:
            raise ValidationError(detail='Found duplicated values!')
        return validated_data

    def create(self, validated_data):
        """Сохраняет объекты в базу"""

        with transaction.atomic():
            created_items = self._bulk_create_items(validated_data)
        return created_items


class ItemSerializer(base_serializers.ModelSerializer):
    """Сериализатор единичного объекта"""

    id = serializers.IntegerField(source='pk', read_only=True)
    value = serializers.CharField(required=True)

    class Meta:
        model = Item
        fields = ('id', 'value',)

    def update(self, instance, validated_data):
        """Обновляет атрибуты объекта"""

        with transaction.atomic():
            instance.value = validated_data.get('value')
            instance.save()
        return instance

