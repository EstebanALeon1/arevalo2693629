class User:
    def __init__(self, nombre, id):
        self.__nombre = nombre
        self.__id = id
   
    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
   
    def setId(self,id):
        self.__id = id
        
    def getId(self):
        return self.__id
    
    def verification(self):
        nombre = input("Digite el nombre: ")
        id = int(input("Digite el id: "))
        if nombre == self.__nombre and id == self.__id:
            print("Verificacion exitosa")
        else:
            print("Verificacion fallida")
                
    def checkAccount(self,id):
        
        if  self.__id == id:
            print("Esta cuenta ya esta creada")
        else:
            print("Esta cuenta no esta creada")
            
    


