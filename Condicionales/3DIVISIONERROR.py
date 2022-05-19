#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

a = int (input ("Dame el valor de a = "))
b = int (input ("Dame el valor de b = "))

if  b == 0:
    print ("SYNTAX ERROR ")
else:
    print ("El resultado es ", (a / b) )    