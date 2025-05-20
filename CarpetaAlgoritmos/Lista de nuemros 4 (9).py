import random

# Paso 1: Creamos la lista con 20 números aleatorios
lista = []
for i in range(20):
    numAleatorio = random.randint(1, 100)
    lista.append(numAleatorio)

print("Lista de números:", lista)

# Paso 2: Pedimos al usuario un número
numUser = int(input("Escribe un número para buscar: "))

# Paso 3: Encontramos el número más grande y contamos apariciones
numMayor = max(lista)
vecesMayor = lista.count(numMayor)

# Paso 4: Contamos cuántas veces aparece el número del usuario
vecesUser = lista.count(numUser)

# Paso 5: Comparamos y devolvemos resultado
if vecesUser > vecesMayor:
    print("Verdadero: El número ingresado aparece más veces que el número mayor.")
else:
    print("Falso: El número ingresado NO aparece más veces que el número mayor.")
2