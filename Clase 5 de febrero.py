import random

#Generar los valores aleatorios con variable nombre que es A y B y maximo_valor el cual es 30
def generar_conjunto(nombre, maximo_valor=30):
    while True:
        try:
            n = int(input("Ingrese la cardinalidad del conjunto: "))
            if 0 <= n <= maximo_valor:
                break
            else:
                print("Entrada inválida, ingrese un número entre 0 y 30.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
#generar el conjunto    
    conjunto = set()
    while len(conjunto) < n:
        conjunto.add(random.randint(0, maximo_valor))
    return conjunto

# Función para A ∪ B
def union(a, b):
    c = set()
    for elemento in a:
        c.add(elemento)
    for elemento in b:
        c.add(elemento)
    return c

# Función para A ∩ B
def interseccion(a, b):
    c = set()
    for elemento in a:
        if elemento in b:
            c.add(elemento)
    return c

#Función para A - B
def diferencia(a, b):
    c = set()
    for elemento in a:
        if elemento not in b:
            c.add(elemento)
    return c

#Función para A △ B (No logre hacer el circulito ese)
def diferencia_simetrica(a, b):
    c = set()
    for elemento in a:
        if elemento not in b:
            c.add(elemento)
    for elemento in b:
        if elemento not in a:
            c.add(elemento)
    return c

#Generar los 2 conjuntos
conjunto_a = generar_conjunto("A")
conjunto_b = generar_conjunto("B")

#Imprimir los 2 conjuntos
print("\nConjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)

#Se generan las variables que son los resultados de sus respectivas operaciones
union_resultado = union(conjunto_a, conjunto_b)
interseccion_resultado = interseccion(conjunto_a, conjunto_b)
diferencia_a_b = diferencia(conjunto_a, conjunto_b)
diferencia_b_a = diferencia(conjunto_b, conjunto_a)
diferencia_simetrica_resultado = diferencia_simetrica(conjunto_a, conjunto_b)

#Se imprimen los resultados de las operaciones
print("\nA ∪ B (Unión):", union_resultado)
print("A ∩ B (Intersección):", interseccion_resultado)
print("A - B (Diferencia A - B):", diferencia_a_b)
print("B - A (Diferencia B - A):", diferencia_b_a)
print("A △ B (Diferencia simétrica):", diferencia_simetrica_resultado)
