#se crea la superclase super 
class Super:
    #constructor de la clase 
    def __init__(self, name):
        self.name = name
    #metodo que retorna el valor del parametro de el contructor y lo imprime de manera legible
    def __str__(self):
        return "Mi nombre es " + self.name + "."

#se crea la subclase sub que hereda de super 
class Sub(Super):
    #se crea el constructor de la clase sub en el cual invoca el constructor de la clase super ademas de agregar un nuevo argumento que es el apellido
    def __init__(self, name,apellido):
        Super.__init__(self, name)
        self.__apellido=apellido

    #metodo en el cual retorna la cadena de __str__ de la superclase super mas __str__ de cla subclase sub 
    def __str__(self):
        return super().__str__()+' '+self.__apellido
    
    
#se instancia un objeto de la clase sub en el cual se especifica nombre y apellido ya que este pertenece a la clase sub retornara ademas de la cadena del nombre la cadena del apellido 
obj = Sub("Andy","Stallman")

#se imprime el objeto retornara el nombre y el apellido 
print(obj)