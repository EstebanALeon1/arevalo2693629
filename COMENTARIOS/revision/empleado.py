#se crea la clase empleado 
class empleado:
    #se crea un contador de objetos
    objetos=0
    #se crea un constructor para la clase con nombre, cargo y salario 
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        empleado.objetos+=1 #se aumenta 1 a objetos cada vez que se crea un objeto

    #metodo que permite ver los nombres
    def getnombre(self):
        return self.__nombre
    
    #metodo que permite modificar el nombre
    def setnombre(self,nombre):
        self.__nombre=nombre

    #metodo que permite ver el cargo
    def getcargo(self):
        return self.__cargo
    
    #metodo que permite modificar el cargo
    def setcargo(self,cargo):
        self.__cargo=cargo

    #metodo que permite ver el salario
    def getsalario(self):
        return self.__salario
    
    #metodo que permite modificar el salario 
    def setsalario(self,salario):
        self.__salario=salario

    #metodo para calcular el salario por hora
    def calcularHora(self):
        horastrabajo=8
        diassemana=5
        diasmes=20
        salariohora=self.salario /(horastrabajo * diassemana * diasmes)
        return self.__salariohora
    
    
