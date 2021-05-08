#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

capital=round(float(input("Cual es el capital a invertir?")),2)
if capital>=0:
    #print("es positivo")
    tasa_anual = 30.2
    print(f"La tasa anual es de {tasa_anual} %")
    periodo=int(input("Cuantos meses quiere invertir el dinero?"))
    capitalfinal=(str(capital*(tasa_anual/100) * periodo/12))
    print(f"Su ganancia en {periodo} meses es de % {capitalfinal}")
else: 
    print("Error numero negativo")
