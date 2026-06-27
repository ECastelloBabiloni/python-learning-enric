# Funciones
def calculadora(horas_realizadas, precio_horas):
    if horas_realizadas > 40:
        horas_extras = horas_realizadas - 40
        horas_normales = horas_realizadas - horas_extras
    else:
        horas_normales = horas_realizadas
        horas_extras = 0

    pago_horas_normales = horas_normales * precio_horas
    pago_horas_extras = horas_extras * (precio_horas * 1.5)

    pago_total = pago_horas_normales + pago_horas_extras

    return pago_horas_normales, pago_horas_extras, pago_total

# Enrtadas
horas_realizadas = int(input("Horas realizadas: "))
precio_hora_trabajada = input("Precio de la hora: [10]")
if precio_hora_trabajada == (""):
    precio_horas = 10
else:
    precio_horas = float(precio_hora_trabajada)

# Llamada y resultados
pago_horas_normales, pago_horas_extras, pago_total = calculadora(horas_realizadas, precio_horas)

# Salida

print("Pago por horas normales: ",pago_horas_normales, "Euros")
print("Pago por horas extras: ", pago_horas_extras, "Euros")
print("Importe total a pagar: ", pago_total, "Euros")