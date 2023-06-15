#se hace la importacion de la clase persona y curso 
from Persona import *
from Curso import *

#aprendiz subclase de persona 
class Aprendiz(Persona):
    #constructor de la clase aprendiz el cual a su vez invoca el constructor de la clase persona para asignar nombre y documento
    #esta clase agrega otros argumentos como la formacion y la ficha 
    def __init__(self,nombre,documento,formacion,ficha):
        Persona.__init__(self,nombre,documento)
        self.__formacion=formacion
        self.__ficha=ficha
        self.__cursos=[]
    
    #metodo para agregar cursos a una lista 
    def agregarCurso(self,curso):
        self.__cursos.append(curso)
    
    #metodo para componer los cursos con su nombre y el tipo 
    def componerCurso(self):
        nombreCurso=input('Ingrese nombre del curso')
        tipoCurso=input('Ingrese tipo del curso')
        objcurso=Curso(nombreCurso,tipoCurso)#se instancia un objeto de la clase curso con sus dos argumentos 
        self.__cursos.append(objcurso)#se adiciona a la lista cursos el objeto 
    
    #metodo que nos permite ver los cursos guardados 
    def verCursos(self):
        return self.__cursos

        