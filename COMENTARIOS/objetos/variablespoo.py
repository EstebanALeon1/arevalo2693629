#se crea una clase 
class Prueba:
        
    contador=0#se crea un contador su funcion es saber cuantos objetos se crearon
    
    #se crea el contructor de la clase 
    def __init__(self,var=1):
        Prueba.contador+=1 #se sumara a 1 al contador cada vez que se cree un nuevo objeto
        self.__var=var
        
    #metodo con otra variable
    def otraVariable(self,var2):
        self.__var2=var2

#se imprime le contador
print(Prueba.contador)

#se instancia ob1 de la clas eprueba 
ob1=Prueba(100)
print(ob1.__dict__,ob1.contador)#se imprime el diccionario con los argumentos y valores de ob1 y se imprime el contador del objeto 1

#se instancia otro objeto 
ob2=Prueba()
ob2.otraVariable(22)#se le asigna a la otra variable un valor 
print(ob2.__dict__,ob2.contador)#se imprime el diccionario con los argumentos y valores de ob1 y se imprime el contador del objeto 1

#se instancia un tercer objeto
ob3=Prueba()
ob3.otraVariable(333)
ob3.tercerVariable=1500
print(ob3.__dict__,ob3.contador)#se imprime el diccionario con los argumentos y valores de ob1 y se imprime el contador del objeto 1


print(Prueba.contador)#se imprime le contador 
#el contador al final queda con un valor de 3 ya que se crearon 3 objetos es decir se ejecuto el constructor 3 veces 