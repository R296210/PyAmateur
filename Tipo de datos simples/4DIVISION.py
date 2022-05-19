n =int( input ("Dame el valor del numerador "))
m =int( input ("Dame el valor del denominador ")) 

c = (n//m)
r = ((n) % (m))

print("La division es " + str(n) + "/" +str( m ))
print("El cociente es " + str (c) + " y el residuo es " + str (r))