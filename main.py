import funciones as f
print("=! Asistente Teoría de Código !=")
print(" 1. Distancia de Hamming entre dos palabras \n 2. Distancia mínima de un código \n 3. Encontrr paráametros de un código \n 4. Decodificar usando distancia mínima")
select = input()

if select=="1":
    print("Ingrese las palabras a calcular la distancia: ")
    p1=input("P1: ")
    p2=input("P2: ")
    #Recordatorio: Acomodar para que no se termine el programa cuando no son de la misma longuitud
    print(f.hamming(p1,p2,0))

if select=="2":
    print("Ingrese el código separando por coma los elementos: ")
    cad=input("C= { ")
    C = cad.split(", ")
    f.dCodigo(C)

