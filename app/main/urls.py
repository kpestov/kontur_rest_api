from django.urls import path

from .views import (
    ItemsCreateView, ItemsView
)

app_name = 'main'

urlpatterns = [
    path('items/create', ItemsCreateView.as_view(), name='items__create'),
    path('items/<int:item_id>', ItemsView.as_view(), name='items'),
]
