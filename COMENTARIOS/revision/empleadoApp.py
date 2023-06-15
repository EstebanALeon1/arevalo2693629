#se importa la clase empleado con todos sus metodos 
from empleado import *

#se instancia un objeto de la clase persona con sus debidos argumentos y valores 
empleado1 = empleado("Jose", "dearrollador", 1160)


print(empleado1.getnombre())#se imprime el nombre
empleado1.setnombre("Juan")#se modifica el nombre
print(empleado1.getnombre())#se imprime el nombre
#print(empleado1.__dict__)

print(empleado1.getcargo())#se imprime el cargo
empleado1.setcargo("arquitecto")#se modifica el cargo
print(empleado1.getcargo())#se imprime el cargo

print(empleado1.getsalario())#se imprime el salario
empleado1.setsalario(2000)#se modifica el salario
print(empleado1.getsalario())#se imprime el salario
#print(empleado1.calcularHora())
print(empleado1.__dict__)#se imprime el diccionario con llaves y valoes de la clase y el objeto