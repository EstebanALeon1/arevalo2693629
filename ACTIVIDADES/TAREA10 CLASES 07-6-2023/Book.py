class Book:
    def __init__(self, isbn, fecha):
        self.__titulo = []
        self.__autor = []
        self.__isbn = isbn
        self.__fecha = fecha
    
    def setTitulo(self,titulo):
        self.__titulo.append(titulo)
        
    def getTitulo(self):
        return self.__titulo
    
    def setAutor(self, autor):
        self.__autor.append(autor)
        
    def getAutor(self):
        return self.__autor
    
    def setIsbn(self,isbn):
        self.__isbn = isbn
        
    def getIsbn(self):
        return self.__isbn
    
    def setFecha(self,fecha):
        self.__fecha = fecha
        
    def getFecha(self):
        return self.__fecha
    
    def duedt(self, autor, titulo):
        if titulo in self.__titulo:
            self.__autor.append(autor)
            print(f"se ha agregado un autor al libro {titulo}")
        else:
            print("Este libro no existe")
    
    def EstadoReservacion(self, estado):
        if estado == True:
            print("Este libro no esta reservado")
        else:
            print("Este libro ya esta reservado")
            
    def Comentario(self):
        comentario = input("Digite el comentario del libro: ")
        return comentario
    
    def SolicitudLirbo(self):
        solicitudlibro = input("Digite el cnobre de quien reserva: ")
        return solicitudlibro

        
            
        
        
        