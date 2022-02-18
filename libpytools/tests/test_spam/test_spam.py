# baby steps, criar o minimo de teste possível, e fazer com que ele passe.
import pytest

from libpytools.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['robson_lsc@hotmail.com','robson_lsc2@hotmail.com']
) # cria o parametro que será aplicado no teste abaixo

def test_rementente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'rlpleao@gmail.com',
        'email spam',
        'Primeiro teste de spam')
    assert remetente in resultado

# cada step deve conter o mínimo de modificações possíveis, para garantir a integralidade do código.


@pytest.mark.parametrize(
    'remetente',
    ['','robson_lsc2hotmail.com']
) # cria o parametro que será aplicado no teste abaixo

def test_rementente_excecoes(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'rlpleao@gmail.com',
            'email spam',
            'Primeiro teste de spam')
