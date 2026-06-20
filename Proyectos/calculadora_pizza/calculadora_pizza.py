pizza = {
    "harina": 500,
    "agua": 325,
    "sal": 12
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