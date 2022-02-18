from unittest.mock import Mock

import pytest

from libpytools.spam.enviador_de_email import Enviador
from libpytools.spam.main import EnviadorDeSpam
from libpytools.spam.modelos import Usuario

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='robson',email='robson_lsc@hotmail.com'),
            Usuario(nome='renzo', email='robson_lsc2@hotmail.com')
        ],
        [
            Usuario(nome='robson',email='robson_lsc@hotmail.com'),
        ]
    ]
)
def test_quantidade_de_spam(sessao,usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'robson_lsc@hotmail.com',
        'Curso Python Pro',
        'Estudando para deixar de ser python noob'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='robson',email='robson_lsc@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'alguem@hotmail.com',
        'Curso Python Pro',
        'Estudando para deixar de ser python noob'
    )
    enviador.enviar.assert_called_once_with(
        'alguem@hotmail.com',
        'robson_lsc@hotmail.com',
        'Curso Python Pro',
        'Estudando para deixar de ser python noob'
    )