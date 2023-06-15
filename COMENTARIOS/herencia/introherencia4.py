#se cre la clase one 
class One:
    #se crea el constructor 
    def do_it(self):
        print("do_it de One")

    #metodo para invocar do_it esto se hace porque en la siguiente clase veremos un metodo nombrado de igual forma esto se llama poliformismo
    def doanything(self):
        self.do_it()

#se clea la clase two 
class Two(One):
    #se define un metodo que es nombrado de la misma forma que el primer metodo de la clase one 
    def do_it(self):
        print("do_it de Two")

#se instancian los objetos uno para cada clase 
one = One()
two = Two()

#se hace una anulacion en el objeto dos esto se llama poliformismo y es la forma de cambiar el comportamiento de una clase ya definida una clase o un metodo puede tomar varios valores 
one.doanything()
two.doanything()

#Polimorfismo en JAVA
# Persona ob=new Persona();
# Medico m=new Medico();

# Persona ob2=new Medico();


