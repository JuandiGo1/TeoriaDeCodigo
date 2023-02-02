#Distancia de Hamming entre dos palabras
def hamming(p1, p2, retornar):
    l1 = len(p1)
    l2 = len(p2)
    d=0
    
    if l1!=l2:
        return "No es posible realizar la operación, ingrese datos con la misma longuitud"
    else:
        
        for i in range(l1):
            if p1[i] != p2[i]:               
                d+=1
        if retornar==0:
            return f"d({p1},{p2}) = {d}"
        if retornar==1:
            return d

def dCodigo(c):
    menor= 999999
    for i in c:
        for j in c:
            I= c.index(i)
            J= c.index(j)
            if c.index(j)> c.index(i) :
                print(hamming(c[I], c[J],0))
                d= hamming(c[I], c[J],1)
                if d < menor:
                    menor= d
    print(f"Distancia minima del código: {d}")

            
