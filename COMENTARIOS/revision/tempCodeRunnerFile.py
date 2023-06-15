#se crea la clase star 
class Star:
    #se crea el contructor de la clase con name y galaxy
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

#se instancia un objeto de la clase con sus dos argumentos 
sun = Star("Sol", "Vía Láctea")

print(sun)#no hay un metodo que nos permita visualizar de una forma entendible el objeto sun este print nos proporciona la ubicacion de la memoria en el que esta guardada el objeto