from django.db import models


class Item(models.Model):
    """
    Модель объекта
    Attributes:
        value - значение объекта
    """
    value = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['value'], name='unique_value')
        ]

    def __str__(self):
        return f'[pk: {self.pk}] [item_value: {self.value}]'
