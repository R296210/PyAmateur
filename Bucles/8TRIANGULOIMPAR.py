alt = int (input ('\n'"Cual es la altura del Triangulo "))

for i in range(1, alt+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print ("")
