i = 1 
sp = 0
si = 0
while i <= 10:
    print(i)
    i += 1
    if i % 2  == 0: 
        sp+=i
    else:
        si+=i
        
print(f"la suma de los numeros impares es igual a {si}")
print(f"la suma de los umeros pares es igual a {sp}")

