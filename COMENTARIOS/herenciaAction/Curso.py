#se crea la clase curso con dos argumentos el nombre y el tipo
class Curso:
    #se crea el constructor con dos argumentos nombre y tipo
    def __init__(self,nombre,tipo):
        self.__nombre=nombre
        self.__tipo=tipo

    #metodo para ver el nombre 
    def getNombre(self):
        return self.__nombre