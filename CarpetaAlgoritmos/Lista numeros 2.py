import random

# Creamos la lista con 20 números aleatorios
lista = []
for i in range(20):
    numero_aleatorio = random.randint(1, 100)
    lista.append(numero_aleatorio)

print("Lista de números:", lista)

# Pedimos el número a buscar
buscado = int(input("¿Qué número quieres buscar?: "))

# Contamos cuántas veces aparece
contador = lista.count(buscado)

if contador > 0:
    # Guardamos todas las posiciones donde aparece
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == buscado:
            posiciones.append(i)
    
    print(f"¡El número {buscado} aparece {contador} veces!")
    print("Posiciones:", posiciones)
else:
    print("Número no encontrado")
