from Access_User_Log import *

tipo_usuario = escolha()
while tipo_usuario != 0:
    logado, usuario, nivel_acesso = login("usuarios.json")
    if logado:
        if tipo_usuario == 1:
            print('Logado: {}, Usuário: {}, Nível de acesso: {}'.format(logado, usuario, nivel_acesso))
            access_log(logado, usuario, arquivo="sys_access.json")
        elif tipo_usuario == 2:
            opcao = escolha('adm')
            while opcao != -1:
                if opcao == 1:
                    print("Listar usuários")
                elif opcao == 2:
                    print("Pesquisar usuarios")
                elif opcao == 3:
                    print("Listar acessos por por data específica")
                else:
                    print("Opção inválida")
                opcao = escolha('adm')
        else:
            print("Opção inválida")

        tipo_usuario = escolha()
    else:
        print("Login incorreto!")


# logado, usuario, nivel_acesso = login("usuarios.json")
# if logado:
#     print('Logado: {}, Usuário: {}, Nível de acesso: {}'.format(logado, usuario, nivel_acesso))
#     # access_log(logado, usuario, arquivo="sys_access.json")
# else:
#     print("Incorreto")
# print(logado)