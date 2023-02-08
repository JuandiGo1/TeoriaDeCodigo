import funciones as f
print("=! Asistente Teoría de Código !=")
print(" 1. Distancia de Hamming entre dos palabras \n 2. Distancia mínima de un código \n 3. Encontrar parámetros de un código \n 4. Decodificar usando distancia mínima")
select = input()

if select=="1":
    print("Ingrese las palabras a calcular la distancia: ")
    p1=input("P1: ")
    p2=input("P2: ")
    #Recordatorio: Acomodar para que no se termine el programa cuando no son de la misma longuitud
    print(f.hamming(p1,p2,0))

#Recordatorio: Validar para cuando cuando no son de la misma longuitud

if select=="2":
    print("Ingrese el código separando por coma y espacio los elementos (ejemplo: 010, 100 ): ")
    cad=input("C= { ")
    C = cad.split(",")
    f.disMinCodigo(C)
    print(f"Distancia minima del código: {f.disMinCodigo(C)}")

if select=="3":
    print("Ingrese el código separando por coma y espacio los elementos (ejemplo: 010, 100 ) : ")
    cad=input("C= { ") 
    print("}")
    C = cad.split(",")
    f.Encontrar_Parametros(C)

if select=="4": 
    print("Ingrese el código separando por coma los elementos: ")
    cad=input("C= { ") 
    print("}")
    C = cad.split(",")
    op=True
    while op==True:
        pal = input("Ingrese la palabra a decodificar: ")
        print(f"Decodificamos {pal} en {f.decodificar(pal,C)}")
        print("1. Continuar decodificando \n 2. Salir")
        elec=input()
        if elec == "2":
            op=False
    
