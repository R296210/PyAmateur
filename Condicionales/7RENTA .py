#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# 5% 10000 . 15% 20000 .  20% 35000  . 30% 60000  45% 60001
#Escribir un programa que pregunte al usuario su renta anual y 
# muestre por pantalla el tipo impositivo que le corresponde.

renta = int (input ("Escriba el monto de su renta anual en € "))

if renta <= 10000:
    opcion = 5
elif renta <= 20000:
    opcion = 15
elif renta <= 35000:
    opcion = 20
elif renta <= 60000:
    opcion = 30
elif renta > 60000:
    opcion = 45
else: 
    print("error")
print ("El impositivo que le corresonde es " , opcion , " %" , "Total a pagar es : " , (renta * (0.01*opcion)), " €")

