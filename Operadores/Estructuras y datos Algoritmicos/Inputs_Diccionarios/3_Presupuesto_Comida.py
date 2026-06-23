comensales = int(input("Numero de personas: "))
precio_por_persona = input("Precio por persona [12]: ")

if precio_por_persona == (""):
    precio_por_comensal = 12
else:
    precio_por_comensal = float(precio_por_persona)

propina_imp = input("Propina del [10%]: ")

if propina_imp == (""):
    propina = 10 / 100
else:
    propina = int(propina_imp) / 100

subtotal = comensales * precio_por_comensal
propina_importe = subtotal * propina
total =  subtotal + propina_importe

print("El subtotal es: ", round(subtotal,2),"Euros")
print("La propina es de: ", round(propina_importe,2),"Euros")
print("El total es de: ", round(total,2),"Euros")