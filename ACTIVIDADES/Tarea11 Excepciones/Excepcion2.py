def Division():
    try:
        Dividendo = int(input("Digite el dividendo: "))
        Divisor = int(input("Digite el divisor: "))
        print(round(Dividendo / Divisor,2))
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except ValueError:
        print("Solo se aceptan valores numericos, valor ingresado incorrecto")
    except:
        print("Error desconocido")
Division()