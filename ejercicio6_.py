# inicializar la variable 'resultado'
resultado = 0


n = int(input("Número de elementos de los vectores: "))


vector1 = [None] * n
print("Elementos del primer vector:")
for i in range(n):
    print("Posición:", i)
    vector1[i] = int(input("Valor: "))


vector2 = [None] * n
print("Elementos del segundo vector:")
for i in range(n):
    print("Posición:", i)
    vector2[i] = int(input("Valor: "))


for i in range(n):
    resultado += vector1[i] * vector2[i]


print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("El producto punto entre los dos vectores es:", resultado)