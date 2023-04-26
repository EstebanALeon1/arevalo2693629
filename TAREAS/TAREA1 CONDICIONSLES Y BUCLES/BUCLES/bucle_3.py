#elaborar un programa en el cual se le pida al usuario una contraseña secreta para salir de un bucle infinito
print("¡PISTA!\nsustancia vital para los seres vivos")
palabra = input("digite una palabra: ")
while palabra != "agua":
    print("palabra incorrecta estas en mi bucle")
    palabra = input("digite una palabra: ")
print("!FELICIDADES¡\nHaz logrado salir del bucle")