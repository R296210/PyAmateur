## PANADERIA DESCUENTO X PAN NO FRESCO 60%
## <> PAN ----> 3.49 € 

v = int (input ("Cuantos panes no fescos se vendieron "))

costo = 3.49
descuento = 0.6
subtotal= costo * v

nc = ( costo * descuento )
d = nc * v
t = subtotal - d

print ("El costo por pieza de pan " + str (costo) + " €")
print ("El descuento sobre una barra no fresca es de 60.0 %")
print ("El total a pagar es  " + str (round (t,2)) + " €")

