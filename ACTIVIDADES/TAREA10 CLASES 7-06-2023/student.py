from user import *

class student (user):
    def __init__ (self,name,id,clase):
        user.__init__(self,name,id)
        self.__clase=clase