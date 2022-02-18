from libpytools.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Robson', email='robson_lsc@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)  # testar se foi craido um id para o usuario salvo


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='robson',email='robson_lsc@hotmail.com'), Usuario(nome='renzo', email='robson_lsc2@hotmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()  # testar se o metodo listar retorna a lista de usuarios criados

