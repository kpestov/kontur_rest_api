import pytest

from app.main.utils import reverse

pytestmark = [pytest.mark.django_db]


def test_items_create_ok(api_client, payload_to_create_items):
    resp = api_client.post(reverse('main:items__create'), payload_to_create_items)
    assert [item['value'] for item in resp.data] == ['one', 'two']
    assert resp.status_code == 201


@pytest.mark.parametrize('invalid_payload', argvalues=[
    ([{'val': 123}, {'value': 'one'}]),
    ([{}, {'value': 'one'}]),
    ({'value': 'qwe123'}),
])
def test_items_create_failed(invalid_payload, api_client):
    resp = api_client.post(reverse('main:items__create'), invalid_payload)
    assert resp.status_code == 400


def test_item_update_failed_not_found(api_client, create_items):
    item_id = 999
    resp = api_client.patch(f'api/item/{item_id}/update', {'value': 'updated_value'})
    assert resp.status_code == 404


def test_items_get_ok(api_client, create_items):
    resp = api_client.get(reverse('main:items'))
    assert [item['value'] for item in resp.data] == ['one', 'two']
    assert resp.status_code == 200
