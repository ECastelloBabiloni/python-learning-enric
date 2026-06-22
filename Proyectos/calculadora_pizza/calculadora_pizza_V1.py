def calcular_harina_desde_total(receta):
    porcentaje_total = receta["hidratacion"] + 100 + receta["porcentaje_sal"]
    peso_harina = receta["peso_total"] * 100 / porcentaje_total

    return peso_harina

def calcular_agua_desde_total(receta):
    harina = calcular_harina_desde_total(receta)
    agua = harina * receta["hidratacion"] / 100
    return agua


def calcular_sal_desde_total(receta):
    harina = calcular_harina_desde_total(receta)
    sal = harina * receta["porcentaje_sal"] / 100
    return sal


def calcular_receta_desde_total(receta):
    masa = {
        "harina": calcular_harina_desde_total(receta),
        "agua": calcular_agua_desde_total(receta),
        "sal": calcular_sal_desde_total(receta)
    }
    return masa


# Configuracion y entrada de usuario

peso_por_persona = 320
porcentaje_sal = 2.4

comensales = int(input("Numero de comensales: "))

entrada_hidratacion = input("Hidratacion [70]: ")
if entrada_hidratacion == "":
    hidratacion = 70
else:
    hidratacion = int(entrada_hidratacion)

peso_total = peso_por_persona * comensales


print("Peso total de la masa: ", peso_total, "g")


receta_usuario = {
    "peso_total": peso_total,
    "hidratacion": hidratacion,
    "porcentaje_sal": porcentaje_sal
}


receta_calculada = calcular_receta_desde_total(receta_usuario)

print("Hidratación: ", hidratacion, "%")
print("Harina:", round(receta_calculada["harina"]), "g")
print("Agua:", round(receta_calculada["agua"]), "g")
print("Sal:", round(receta_calculada["sal"]), "g")