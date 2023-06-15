#se crea la clase persona 
class Persona:
    #se crea el constructor de la clase con dos argumentos nombre y documento
    def __init__(self,nombre,documento):
        #print('Se instancio un objeto')
        self.__nombre=nombre
        self.__documento=documento
        #self.__telefono
        self.__cursos=[]
        
    #metodo que permite modificar el nombre 
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    #metodo que permite ver el nombre 
    def getNombre(self):
        return self.__nombre
    