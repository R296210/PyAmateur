
puntos = float (input ("Puntuacion del usuario "))

if puntos == 0.0:
    print ("Nivel de rendimiento es Inaceptable "'\n', " Cantidad recibida es ", puntos*2400," €")
elif puntos == 0.4:
    print ("Nivel de rendimiento es Aceptable " '\n', " Cantidad recibida es ", puntos*2400," €")
elif puntos >= 0.6:
    print ("Nivel de rendimiento es Meritorio "'\n', " Cantidad recibida es ", puntos*2400," €")
else:
    print ("Error ")
