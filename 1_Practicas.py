db_usuarios = {"brais": "1234", "roberto": "pypass", "enric": "admin"}
intentos_fallidos = {"brais": 0, "roberto": 0, "enric": 0}

def validar_acceso(usuario, password_intentada):
    
    if usuario not in db_usuarios:
        return "Usuario no existe"
    
    if intentos_fallidos[usuario] >= 3:
        return "Usuario bloqueado"
    
    if password_intentada == db_usuarios[usuario]:
        intentos_fallidos[usuario] = 0
        return "Bienvenido al sistema"
    
    else:
        intentos_fallidos[usuario] += 1
        return "Contraseña incorrecta"
    

usuario = "brais"
password_intentada = "1234"

print(validar_acceso(usuario, password_intentada))