from django.urls import path

from .views import (
    ItemsCreateView,
)

app_name = 'main'

urlpatterns = [
    path('items/create', ItemsCreateView.as_view(), name='items__create'),
]
