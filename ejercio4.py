n = int(input("Escriba un número positivo: "))
m = int(input("Escriba un número positivo: "))
if n < 0 :
    print("Por favor coloque un número positivo")
else:
    if m < 0:
        print("Por favor coloque un número positivo")
    else:
        
        c =(n//m)
        r=(n%m)
        print("El cociente de la división es",c, ", mientras que el resto es",r)
        print(f"El resultado de la división de {n} sobre {m} da como cociente {c} y como resto {r} ")
        
         