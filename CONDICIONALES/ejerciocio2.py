horastrabajadas= int(input("Cuantas horas trabajaste?"))
salario= float(input("Cuanto es tu salario por hora?"))
if horastrabajadas >40:
    sueldo = ((salario  * horastrabajadas) + ((salario*1.5) * (horastrabajadas-40)))
    print (f"El sueldo es ${sueldo}")
else:
    sueldo=horastrabajadas*salario
    print (f"El sueldo es ${sueldo}")
    