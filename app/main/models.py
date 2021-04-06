from django.db import models


class Storage(models.Model):
    """
    Модель хранилища данных
    Attributes:
        key - ключ объекта из хранилища
        value - значение объекта из хранилища
    """
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'[pk: {self.pk}] [storage_key: {self.key}] [storage_value: {self.value}]'
