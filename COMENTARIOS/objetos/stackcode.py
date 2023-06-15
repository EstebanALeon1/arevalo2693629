#se crea una clase la cual su funcionamiento sera una pila(ultimo en entrar, primero en salir)(LIFO)
class Stack:
    #se cera el constructor de la lista con una lista para la pila 
    def __init__(self):
        self.__stack_list = []

    #se crea un metodo para agregar elementos a la liista mediante val que sera el primer argumento y append que agregara val al final de la lista 
    def push(self, val):
        self.__stack_list.append(val)

    #se crea un metodo para eliminar el ultimo elemento de la lista que se hace mediante la lista accediento al ultimo elemento con indices negativos y se elimina utilizando del val sera utilizado para mostrar en pantalla el elemento que se elimino 
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


#se crea una clase la cual es una subclase de stack
class AddingStack(Stack):
    #constructor de la clase el cual invoca al constructor de su superclase y adiciona sum
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    #este metodo permite ver en pantalla sum 
    def get_sum(self):
        return self.__sum

    #este metodo es para agregar elementos a la lista utiliza el metodo definido en la clase stack y aqui se adiciona que todos los elementos que se agregen se vayan sumando y se guarden en sum
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    #se define el metodo pop que utiliza el metodo pop de la superclase y cada vez que se utilice se le resta a sum el elemnto eliminado se utiliza val par mostrar en pantalla el elemnto eliminado 
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


#se instancia un objeto de la subclase 
stack_object = AddingStack()

#este for agregara los elementos de 0 a 5 y los sumara a sum
for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

#este for eliminara los elementos de 0 a 1 y los restara de sum
for i in range(5):
    print(stack_object.pop())
