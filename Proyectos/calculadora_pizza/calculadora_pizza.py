pizza = {
    "harina": 500,
    "agua": 325,
    "sal": 12,
    "hidratacion": 65,
    "porcentaje_sal": 2.4,
    "peso_total": 837
}

print(pizza["harina"])
print(pizza["agua"])
print(pizza["sal"])

def calcular_hidratacion(receta):
    return (receta["agua"]/receta["harina"]) * 100

print("la hidratacion es: ", calcular_hidratacion(pizza))

def calcular_porcentaje_sal(receta):
    return (receta["sal"]/receta["harina"])*100
    
print("el porcentaje de sal es: ", calcular_porcentaje_sal(pizza))

def calcular_agua(receta):
    return (receta["harina"]*receta["hidratacion"])/100

print("la cantidad de agua es: ", calcular_agua(pizza))

def calcular_sal(receta):
    return (receta["harina"]*receta["porcentaje_sal"])/100

print("la cantidad de sal es: ", calcular_sal(pizza))

def calcular_peso_total(receta):
    return receta["harina"]+receta["sal"]+receta["agua"]

print("El peso total de la masa es: ", calcular_peso_total(pizza))

def calcular_harina_desde_total(receta):
    porcentaje_total = receta["hidratacion"] + 100 + receta["porcentaje_sal"]
    peso_harina = receta["peso_total"] * 100 / porcentaje_total

    return peso_harina

print("El peso total de la harina es: ", calcular_harina_desde_total(pizza))

def calcular_agua_desde_total(receta):
    harina = calcular_harina_desde_total(receta)
    agua = harina * receta["hidratacion"] / 100
    return agua

print("cantidad de agua total es: ", calcular_agua_desde_total(pizza))

def calcular_sal_desde_total(receta):
    harina = calcular_harina_desde_total(receta)
    sal = harina * receta["porcentaje_sal"] / 100
    return sal

print("calcula la sal teniendo en cuenta el total: ", calcular_sal_desde_total(pizza))

def calcular_receta_desde_total(receta):
    masa = {
        "harina": calcular_harina_desde_total(receta),
        "agua": calcular_agua_desde_total(receta),
        "sal":  calcular_sal_desde_total(receta)
    }
    return masa

print("diccionario masa: ", calcular_receta_desde_total(pizza))

# A partir de aqui pruebo de hacer V1

peso_por_persona = 320
porcentaje_sal = 2.4

comensales = int(input("Numero de comensales: "))
hidratacion = int(input("Hidratacion: "))

peso_total = peso_por_persona * comensales


print(peso_total)


receta_usuario ={
    "peso_total": peso_total,
    "hidratacion": hidratacion,
    "porcentaje_sal": porcentaje_sal
}
