from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import ValidationError

from app.main import base_serializers
from app.main.models import Item


class ItemListSerializer(serializers.ListSerializer):
    def _bulk_create_items(self, validated_items):
        return Item.objects.bulk_create([
            Item(value=validated_item_data.get('value'))
            for validated_item_data in validated_items
        ])

    def validate(self, validated_data):
        duplicates = Item.objects.filter(value__in=[item.get('value') for item in validated_data])
        if duplicates:
            raise ValidationError(detail='Found duplicated values!')
        return validated_data

    def create(self, validated_data):
        with transaction.atomic():
            created_items = self._bulk_create_items(validated_data)
        return created_items


class ItemSerializer(base_serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    value = serializers.CharField(required=True)

    class Meta:
        model = Item
        fields = ('id', 'value',)
