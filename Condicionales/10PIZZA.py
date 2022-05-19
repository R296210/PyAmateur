resp = str ( input (" PRECIONA (V) PARA PIZZA VEGANA \n PRECIONA (N) PARA PIZZA NORMAL: "))


if resp.upper() == 'V':
    print ("PIZZA VERGANA")
    ingv = input ("\n\t1- PIMIENTO" + "\n\t2- TOFU \n")
    if ingv == '1':
        print ("PIZZA VERGANA: PIMIENTO,MOZZARELLA Y TOMATE.")
    elif ingv == '2':
        print ("PIZZA VERGANA: TOFU,MOZZARELLA Y TOMATE.")
    else:
        print ("ERROR VULVE A INTENTAR")
elif resp.upper() == 'N':
    print ("PIZZA NORMAL")
    ingn = input ("\n\t1- PEPERONI" + "\n\t2- JAMON" + "\n\t3- SALMON \n")
    if ingn == '1':
        print ("PIZZA NORMAL: PEPERONI, MOZZARELLA Y TOMATE.")
    elif ingn == '2':
        print ("PIZZA NORMAL: JAMON, MOZZARELLA Y TOMATE. ")
    elif ingn == '3':
        print ("PIZZA NORMAL: SALMON, MOZZARELLA Y TOMATE. ")
    else:
        print ("ERROR VULVE A INTENTAR")
else:
    print ("ERROR VULVE A INTENTAR")
