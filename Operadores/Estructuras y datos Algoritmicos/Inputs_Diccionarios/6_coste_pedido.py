# Funciones
def calculadora(precio, cantidad, gastos_envio):
    subtotal = precio * cantidad
    if subtotal >= 50:
        gastos_envio = 0

    total_final = subtotal + gastos_envio

    return subtotal, gastos_envio, total_final
    
# Entradas
precio = float(input("Precio del producto: "))
cantidad = int(input("Unidades: "))
coste_envio = input("Gastos de envio [5 Euros]:")

if coste_envio == (""):
    gastos_envio = 5
else:
    gastos_envio = float(coste_envio)

# Llamada y resultados

subtotal, gastos_envio, total_final = calculadora(precio, cantidad, gastos_envio)

# Salida

print("Subtotal: ", subtotal,"Euros")
print("Coste del envio: ", gastos_envio, "Euros")
print("Total: ", total_final,"Euros")
