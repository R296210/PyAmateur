cantidad = input ("Cantidad en EUROS del producto ")
print( cantidad[:cantidad.find('.')] , "EUROS " , cantidad[cantidad.find('.')+1:] , " CENTIMOS ")