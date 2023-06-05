class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setDocumento(self, documento):
        self.__documento = documento
    
    def getDocumento(self):
        return self.__documento
    
    def setCursos(self, cursos):
        self.__cursos.append(cursos)

    def getCursos(self):
        return self.__cursos
    
    def deleteCursos(self, cursos):
        if cursos in self.__cursos:
            self.__cursos.remove(cursos)
        else:
            print("Este curso no existe")

