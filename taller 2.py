def capturar_conjunto(nombre):
    print(f"\n--- Configuración del Conjunto {nombre} ---")
    while True:
        try:
            cardinalidad = int(input(f"¿Cuántos elementos tiene el conjunto {nombre}?: "))
            if cardinalidad < 0:
                print("La cardinalidad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Error: Ingresa un número entero.")

    elementos = set()
    for i in range(cardinalidad):
        item = input(f"  > Ingrese el elemento {i+1}: ")
        elementos.add(item)
    return elementos

# Entrada de datos
U = capturar_conjunto("Universal (U)")
A = capturar_conjunto("A")

# Verificación de subconjunto
print("\n" + "="*40)
es_subconjunto = A.issubset(U)

if es_subconjunto:
    print("A es subconjunto de U (A ⊆ U)")
    
    # Realización de las operaciones:
    #(U - A) ⊕ A  (Diferencia simétrica entre el complemento de A y A)
    op1 = (U - A) ^ A
    
    #(U ∩ A) - A  (Intersección de U y A, menos los elementos de A)
    op2 = (U & A) - A
    
    #(U ∪ A) ∩ A  (Unión de U y A, interceptado con A)
    op3 = (U | A) & A

    print("\nRESULTADOS DE LAS OPERACIONES:")
    print(f"a) (U - A) ⊕ A = {op1 if op1 else '∅ (Conjunto vacío)'}")
    print(f"b) (U ∩ A) - A = {op2 if op2 else '∅ (Conjunto vacío)'}")
    print(f"c) (U ∪ A) ∩ A = {op3 if op3 else '∅ (Conjunto vacío)'}")

else:
    print("A NO es un subconjunto de U.")
    print("Las operaciones no se pudieron realizar.")
print("="*40)