from unittest.mock import Mock
import pytest

from libpytools import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/98554464?v=4'
    resp_mock.json.return_value = {
        'login': 'RLS400',
        'id': 98554464,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpytools.github_api.requests.get')  # mocker restaura a lib no final da função
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('RLS400')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('reclosedev')
    assert 'https://avatars.githubusercontent.com/u/660112?v=4' == url
