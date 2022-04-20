from datetime import datetime
import platform
import getpass
import random
import json
import os


def escolha(tipo_user='usuario'):
    if tipo_user == 'usuario':
        opcao = int(input("[1] Entrar como usuário\n"+
                        "[2] Entrar como administrador\n"+
                        "O que deseja fazer? ([0] Encerra): "))
    if tipo_user == 'adm':
        opcao = int(input("[1] Listar usuários\n"+
                          "[2] Pesquisar usuário\n"+
                          "[3] Listar acessos\n"+
                          "O que deseja fazer? ([-1] Retornar): "))
    return opcao


# carrega os dados para um dicionario de dados
def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_dados:
            dicionario = json.load(arq_dados)
    else:
        dicionario = {}
    return dicionario


# grava no json os dados registrados no dicionario
def gravar_dados(dicionario, arquivo):
    with open(arquivo, "w") as arq_dados:
        json.dump(dicionario, arq_dados)


# Mecanismo de login
def login(arquivo):
    # trás os dados do usuário do json para o dicionario de dados
    dicionario = carregar_dados(arquivo)

    [usuario, senha] = [input("Informe seu login de acesso\nUsuário: "),
                        getpass.getpass("Senha: ")]

    validado, username, nivel_acesso = [False, '', '']
    for chave, valor in dicionario.items():
        if senha == chave and usuario == valor[0]:
            [validado, username, nivel_acesso] = [True, usuario, valor[2]]
            # return True, usuario, valor[2]
    return validado, username, nivel_acesso


# Mecanismo que add no dic
def access_log(access, usuario, arquivo):
    if access:
        dicionario = carregar_dados(arquivo)

        [nome_maq, so, versao, usuario_so, data_hora] = [
            platform.node(), platform.system(),
            platform.version(), getpass.getuser(),
            datetime.now()
        ]

        # gera um id aleatório para cada acesso
        _id = ''
        for x in range(0, 3):
            _id = _id + str(random.randrange(10, 99))

        # TAREFA: ATRIBUIR OUTRA CHAVE {EXP: USUÁRIO+VALOR_ALEATÓRIO}
        dicionario[usuario + _id] = [nome_maq, so, usuario_so, versao, str(data_hora)]

        # chama a função que grava o log no json
        gravar_dados(dicionario, arquivo)
        print(dicionario)
