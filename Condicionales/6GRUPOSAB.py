#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
# y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y 
# muestre por pantalla el grupo que le corresponde.

sexo =   input ("SEXO Hombre (H) o Mujer M): ")
nombre =  input ("NOMBRE: ")

if sexo == "M" : #PREGUNTA SI ES MUJER #
    if nombre.lower() <'m':
        opcion = "A"
    else: 
        opcion = "B"
else: #QUIERE DECIR QUE ES H HOMBRE # 
    if nombre.lower() > 'n':
        opcion = "A"
    else:
        opcion = "B"
print ("Hola ", nombre ," eres del grupo " + opcion )
