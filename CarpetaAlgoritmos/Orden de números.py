numeros = []

for i in range(5):
    num = int(input(f"Escribe el número {i+1}: "))
    numeros.append(num)

numeros.sort(reverse=True)

print("Los números ordenados del más grande al más pequeño son:")
for num in numeros:
    print(num)
