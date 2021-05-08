km_recorrido=int(input("Cuantos kilometros recorrio?"))
monto_fijo = 30000
iva = 0.21
if km_recorrido <= 300:
    montopag= monto_fijo
    print(f"El costo de su viaje es $ {monto_fijo}")
else: 
    if km_recorrido<=1000:
        montopag= monto_fijo+(15* (km_recorrido-300))
        print(f"El costo de su viaje es $ {montopag}")
    else:
        montopag= (monto_fijo+(15*700)+10*(km_recorrido-1000))   
        print(f"El costo de su viaje es $ {montopag}")


montoconiva= (montopag+ (iva * montopag))
impuesto= (iva * montopag)
print(f"El costo final con IVA es $ {montoconiva}, siendo $ {impuesto} de IVA")