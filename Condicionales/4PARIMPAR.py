#Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es par o impar.

dato = int (input ("Ingresa un numero entero "))

if dato % 2 == 0:
    print ("El numero " , dato, " es par ")
else:
    print ("El numero " , dato, " es impar ")