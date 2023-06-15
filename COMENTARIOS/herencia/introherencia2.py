#se crea la clase SampleClass
class SampleClass:
    #se crea el constructor de la clase
    def __init__(self, val):
        self.val = val

#se instancian dos objetos y se crea uno tercero el cual es igual al objeto numero 1
object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1 #se le suma 1 a la variable val del objeto 3 que es igual al objeto 1

#is se utiliza para verificar si nos elementos hacen referencia a la misma clase 
print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val) #se imprimen los valores de val de cada objeto ya que el objeto 3 es igual al objeto uno este tomara su mismo valor de val 


#se crean variables que almacenan strings 
string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"
print(string_1)
print(string_2)

#se verifican las variables con is para saber si estas se refieren a la misma parte de la memoria o a la misma informacion 
print(string_1 == string_2, string_1 is string_2)