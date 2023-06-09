class user:
    def __init__ (self,name,id):
        self.__name=name
        self.__id=id

    def verificar(self,student,instructor):
        return self.__name, self.__id, self.__clase, self.__dept

