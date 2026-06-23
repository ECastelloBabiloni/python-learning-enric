
numero_adultos = int(input("Numero de dultos: "))

numero_ninos = int(input("Numero de ninos: "))

entrada_precio_adulto = input("Precio adulto [10]: ")

if entrada_precio_adulto == (""):
    precio_adulto = 10
else:
    precio_adulto = int(entrada_precio_adulto)

entrada_precio_nino = input("Precio nino [6]: ")

if entrada_precio_nino == (""):
    precio_ninos = 6
else:
    precio_ninos = int(entrada_precio_nino)

total_adultos = precio_adulto * numero_adultos
total_ninos = precio_ninos * numero_ninos
total_entradas = total_adultos + total_ninos

print("El precio total de las entradas es: ", total_entradas, "Euros")