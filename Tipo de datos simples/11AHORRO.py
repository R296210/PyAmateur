##CUENTA DE AHORROS 4% DE INTERES/AÑO EXC.11 PYTHON

d = float (input ("Cuanto dinero deposito "))
o = float (0.04*d)
pa =float ( round ((d + o) ,2))
o2 =float (0.04*pa)
sa =float ( round ((pa + o2),2))
o3 =float (0.04*sa)
ta =float ( round ((sa + o3),2))

print ("El primer año ahorraste ",pa)
print ("El segundo año ahorraste ",sa)
print ("El tercer año ahorraste ",ta)