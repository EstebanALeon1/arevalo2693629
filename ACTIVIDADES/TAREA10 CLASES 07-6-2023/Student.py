from User import *
class Student(User):
    def __init__(self, nombre, id, curso):
        User.__init__(nombre, id)
        self.__curso = curso
        
    def setCurso(self,curso):
        self.__curso = curso
        
    def getNombre(self):
        return self.__curso