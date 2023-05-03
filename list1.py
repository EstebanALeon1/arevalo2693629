lista = [1, 1.4, "sena", ["a", "b",], "soacha" ]
#print(f"elemento {lista[4]}")
print(type(lista))
print(len(lista))
print(f"ultimo {lista[-1]}")


lista.append(20)
lista.append("python")
print(lista)
lista.insert(len(lista), "java")
print(lista)
