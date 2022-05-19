inversion = float (input ("Valor de la inversion: "))
interes = float (input ("Interes anual: "))
años = int (input ("Años invertidos: "))

interes2 = float (interes / 100 )
for i in range (1, años + 1 , 1 ):
    inversion += inversion  * interes2
    print (inversion , end = "\n ")




