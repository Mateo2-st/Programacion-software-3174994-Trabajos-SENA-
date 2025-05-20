import random

# Crear una lista con 20 números aleatorios entre 1 y 100
lista = []
for i in range(20):
    numeroAleatorio = random.randint(1, 100)
    lista.append(numeroAleatorio)

print("Lista de números:", lista)

# Paso 1: Encontrar el número mayor
numeroMayor = max(lista)

# Paso 2: Contar cuántas veces aparece el número mayor
cantidad = lista.count(numeroMayor)

# Paso 3: Mostrar el resultado
print(f"El número más grande es {numeroMayor} y aparece {cantidad} veces.")
