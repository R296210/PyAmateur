prodname = input ("Producto ")
preprod = float (input ("Precio del producto "))
numunid = int (input ("Numero de unidades "))

print('Producto {prodname}: {numunid:3d} U  a {preprod:9.2f} € c/u  Total={total:11.2f} €'.format(prodname = prodname, numunid= numunid, preprod = preprod,total=numunid*preprod))
