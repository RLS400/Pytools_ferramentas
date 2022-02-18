import pytest

from libpytools.spam.db import Conexao


@pytest.fixture(scope='module') # com esse escopo, a fixture só sera execuda uma vez por modulo.
def conexao():
    conexao_obj = Conexao() #SetUp
    yield conexao_obj
    conexao_obj.fechar()  # fechar conexao #TearDown


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao() #SetUp
    yield sessao_obj
    sessao_obj.roll_back()  # desfazer alterações para evitar inteferencia entre testes. #TearDown
    sessao_obj.fechar()  # fechar sessao