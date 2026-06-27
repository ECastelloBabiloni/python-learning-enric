

# Funciones
def calcular(peso, urgente):
    if peso <= 1:
        precio = 5
    elif peso > 1 and peso <= 5:
        precio = 8
    else:
        precio = 12

    if urgente:
        suplemento = 4
    else:
        suplemento = 0

    total_envio = precio + suplemento
    
    return precio, suplemento, total_envio

# Entradas
peso = float(input("Peso: "))
respuesta = (input("Envio urgente: [s/n]")).strip().lower()
urgente = respuesta == "s"

# Llamada y resultados
precio, suplemento, total_envio = calcular(peso, urgente)

# Salida
print("Precio envio: ", precio)
print("Suplemento del envio: ", suplemento)
print("Precio Total envio", total_envio)
