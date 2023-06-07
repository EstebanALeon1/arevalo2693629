from Empleado import *

ob1  =Empleado("Jose", "Administrador", 2160000)

print(ob1.getNombre())
print(ob1.getCargo())
print(ob1.getSalario())
print(ob1.getgananciasHora())
print(ob1.getIncreentoSalarioIPC())
print(ob1.getHorasExtra(25))




print(Empleado.contador)