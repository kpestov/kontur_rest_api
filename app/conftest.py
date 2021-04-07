import pytest

from django.apps import apps
from rest_framework.test import APIClient

from app.main.utils import reverse


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_createdb, django_db_blocker):
    if not django_db_createdb:
        return

    with django_db_blocker.unblock():
        models_to_delete = [
            *apps.get_app_config('main').get_models()
        ]

        for model in models_to_delete:
            if model._meta.managed:
                model._default_manager.all().delete()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def payload_to_create_items():
    return [{"value": "one"}, {"value": "two"}]


@pytest.fixture
def create_items(api_client, payload_to_create_items):
    api_client.post(reverse('main:items__create'), payload_to_create_items)
