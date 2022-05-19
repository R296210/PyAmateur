i= float(input ("Inversión "))
p= float(input ("Interés por año "))
a= int(input ("Años Invertidos "))

e1 = ((p * 0.01) * i ) 
e2 = ((i + e1)* a)

print("Capital de Inversión por " + str(a) + " años es " + str(e2))
