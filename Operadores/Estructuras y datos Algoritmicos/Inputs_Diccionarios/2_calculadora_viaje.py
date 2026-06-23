kilometros = int(input("Kilometros del viaje: "))
consumo = int(input("Consumo en litros/100km: "))

precio_combustible = input("Precio combustible [1.60]: ")

if precio_combustible == (""):
    precio_litro = 1.60
else:
    precio_litro = float(precio_combustible)

litros_consumidos = kilometros * consumo / 100
coste_combustible = litros_consumidos * precio_litro

print("El precio del combustible consumido es: ", coste_combustible,"Euros")