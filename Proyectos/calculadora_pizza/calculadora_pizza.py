pizza = {
    "harina": 500,
    "agua": 325,
    "sal": 12
}

print(pizza["harina"])
print(pizza["agua"])
print(pizza["sal"])

def calcular_hidratacion(pizza):
    return (pizza["agua"]/pizza["harina"]) * 100

print("la hidratacion es: ", calcular_hidratacion(pizza))




