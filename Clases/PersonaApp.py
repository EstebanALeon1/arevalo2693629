from Persona import *
ob1 = Persona("Daniela", 654321)
print(type(ob1))
print(ob1.getNombre())

ob1.setNombre(100)
print(ob1.getNombre())

ob1.setCursos("pepe")
print(ob1.getCursos())

ob1.setCursos("cur")
print(ob1.getCursos())

ob1.setCursos("poph")
print(ob1.getCursos())

ob1.deleteCursos("pepe")
print(ob1.getCursos())

ob1.deleteCursos("pepita")
