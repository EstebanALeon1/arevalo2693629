#Escriba una clase Empleado que tenga como propiedades nombre, cargo, salario
class Empleado:
    contador = 0
    def __init__(self,nombre,cargo,salario):
        Empleado.contador += 1
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario = salario

#escriba metodos contructores, setters y getters  
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setCargo(self,cargo):
        self.__cargo = cargo
    
    def getCargo(self):
        return self.__cargo
    
    def setSalario(self,salario):
        self.__salario = salario
    
    def getSalario(self):
        return self.__salario
    
#escriba un método que permita calcular cuanto gana el empleado en una hora
    def getgananciasHora(self):
        ganancias_dia = self.__salario/30
        return round(ganancias_dia/8, 2)

#un método para saber cuanto recibe de incremento si el salario sube con el IPC
    def getIncreentoSalarioIPC(self):
        #incrementosalario
        if self.__salario <= 1160000:
            incrementosalario = self.__salario * 0.1582
        else:
            incrementosalario = self.__salario * 0.1282
        return incrementosalario
       # mensaje_final = print(f"El incremento del salario es {incrementosalario} y el sueldo total es de {incrementosalario + self.__salario}")

#Un método que reciba una cantidad de horas extras y calcule el salario incrementando las extras.
    def getHorasExtra(self, horasextra):
        if horasextra < 20:
            ValorHoraExtra = self.__salario/240
            return ValorHoraExtra * 1.25 * horasextra
        else:
            return "ha trabajado mas de dos horas diarias esto no es permitido"


