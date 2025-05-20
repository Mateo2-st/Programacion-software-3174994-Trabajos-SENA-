inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))

suma = 0

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma += numero

print(f"La suma de los números pares entre {inicio} y {fin} es: {suma}")
