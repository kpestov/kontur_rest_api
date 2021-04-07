import pytest

from unittest.mock import patch

from app.main.utils import reverse


@patch('app.main.views.ProxyView.upstream', new='https://kats1.skbkontur.ru/api_test/test.json')
def test_proxy_ok(api_client):
    resp = api_client.get(reverse('main:proxy'))
    assert resp.status_code == 200
    assert resp.data == "{['qwe': 123]}"
