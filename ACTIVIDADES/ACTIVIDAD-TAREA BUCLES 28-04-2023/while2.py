#Calcular la operación x n sin utilizar la función pow
base = int(input("Digite un numero base: "))
exponente = int(input("Digite un numero exponente: "))
resultado = base
while exponente > 1:
    resultado = resultado * base
    exponente -= 1

print(f"El resultado de {base} elevado a {exponente} es igual a {resultado}")
