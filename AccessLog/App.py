from Access_User_Log import *

logado, usuario = login("usuarios.json")
if logado:
    print("Logado!")
    access_log(logado, usuario, arquivo="sys_access.json")
else:
    print("Incorreto")
