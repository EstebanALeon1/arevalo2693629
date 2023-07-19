def numero_primo():
    try:
        num_primo = 0
        numero_usuario = int(input("Digite el numero hasta cual quiera saber si es primo: "))
        for i in range(1, numero_usuario+1):
            if numero_usuario % i == 0:
                num_primo += 1
        
        if num_primo == 2:
                print("Este numero es primo")
    
        if num_primo > 2:
                print("Este numero no es primo")
    except ValueError:
         print("El valor ingresado debe de ser numerico, se ingreso un cararter incorrecto")
    except:
         print("Error desconocido")
numero_primo()