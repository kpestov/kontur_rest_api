from django.urls import path

from .views import (
    ItemsCreateView, ItemsView, ItemUpdateView, ProxyView
)
from ..storage.yasg import urlpatterns as doc_urls

app_name = 'main'

urlpatterns = [
    path('items/create', ItemsCreateView.as_view(), name='items__create'),
    path('items', ItemsView.as_view(), name='items'),
    path('item/<int:item_id>/update', ItemUpdateView.as_view(), name='item__update'),
    path('proxy', ProxyView.as_view(), name='proxy'),
]

urlpatterns += doc_urls
