#Para tributar un determinado impuesto se debe ser mayor de 16 años 
# y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
# y muestre por pantalla si el usuario tiene que tributar o no.

edad = int (input ("Edad "))
ingresos_mes = float (input ("Ingresos que persive en € por mes " ))
if edad <= 16 or ingresos_mes < 1000:
#if edad > 16 and ingresos_mes >= 1000: 2 formas de poner la condicion 
#if edad > 16 and ingresos_mes >= 1000:
    print ("NO tiene que cotizar")
else: 
    print ("SI tiene que cotizar")

