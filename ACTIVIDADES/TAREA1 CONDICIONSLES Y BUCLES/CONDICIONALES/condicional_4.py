#realizar un sistema para una tienda virtual de una licoreria la cual pida la edad del usuario si este es mayor de edad le mostrata la opciones de licor que hay disponibles, de lo contrario arrojara un mensaje de advertencia de la venta de licor a menores de edad
edad = int(input("Ingrese su edad: "))
if edad >=18:
    print("1- aguardiente\n2- cerveza\n3- ron\n4- whisky\n5- tequila")
else:
    print('La normativa en el artículo 1 dice que, "prohíbase el expendio de bebidas embriagantes a menores de edad" regrese cuando tenga la edad permitida segun la ley')