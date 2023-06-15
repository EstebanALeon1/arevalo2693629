#Se crea la clase star 
class Star:
    #constructor de la clase star con dos argumentos
    def __init__(self, name, galaxy):
        self.name = name #se define el nomnre que es igual al primer parametro  
        self.galaxy = galaxy #se define galaxy que es igual al segundo para,etro

    # se define un metodo el cual retornara el nombre y la galaxia 
    def __str__(self):
        return self.name + ' en ' + self.galaxy

#se crea un objeto de la clase star con los dos parametros 
sun = Star("Sol", "Vía Láctea")
#se imprime el objeto sun 
print(sun)