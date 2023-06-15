#se importa la clase persona con todos sus metodos 
from Persona import *
ob1=Persona('Daniela',654321)#se instancia ob1 de la clase persona con sus dos argumentos 
print(type(ob1))#se imprime el tipo dle onjeto 
print(ob1.getNombre())#nos muestra el nombre que esta dejinido para ob1
ob1.setNombre(100)#se modifica el nombre que tiene ob1
print(ob1.getNombre())#nos muestra el nombre que esta dejinido para ob1
print(ob1.__dict__)#este metodo imprime un diccionario con la llave definidas como los argumentos de la misma clase y como valores los valores que se le pasan en el objeto