#Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario indique al inicio del programa.
cantidad_digitos  =int(input("Digite el numero de elementos en la serie fibonacci: "))
lista_1 = []
def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
    
for x in range(cantidad_digitos):
    lista_1.append(fib(x))
print(lista_1)