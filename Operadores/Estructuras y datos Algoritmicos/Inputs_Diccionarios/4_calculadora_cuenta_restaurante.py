comensales = int(input("Numero de comensales: "))
precio_por_persona = input("Precio por persona [12]: ")
if precio_por_persona == (""):
    precio_comensal = 12
else:
    precio_comensal = float(precio_por_persona)    

porcentaje_propina = input("Porcentaje propina [10%]: ")
if porcentaje_propina == (""):
    propina = 10 / 100
else:
    propina = int(porcentaje_propina) / 100

def calcular_presupuesto(comensales, precio_comensal, propina):
    subtotal = comensales * precio_comensal
    importe_propina = propina * subtotal
    total_final = subtotal + importe_propina

    return subtotal, importe_propina, total_final
subtotal, importe_propina, total_final = calcular_presupuesto(comensales, precio_comensal, propina)
"""
    cuenta = {
            "subtotal": comensales * precio_comensal,
            "importe propina": propina * subtotal,2
            "total": subtotal + importe_propina
        }
    return cuenta
"""
print(round(subtotal,2), round(importe_propina,2), round(total_final,2))



