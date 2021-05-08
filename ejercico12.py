print( "Hola buen dia, elija la opcion que prefiera : 1-Pan de ayer   2- Pan de hoy")
respuesta= (input())
if respuesta == "1":
    cantidadbarras= int((input("Cuantas barras de pan quiere?")))
    total= float(((3.49 * cantidadbarras)* 0.60))    
    print(f"El precio total de su compra es $ {total}")
else: 
    cantidadbarras= int((input("Cuantas barras de pan quiere?")))
    total= float(3.49 * cantidadbarras)   
    print(f"El precio total de su compra es $ {total}")
    