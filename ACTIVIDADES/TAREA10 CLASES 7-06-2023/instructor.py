from user import *

class instructor (user):
    def __init__ (self,name,id,dept):
        user.__init__(self,name,id)
        self.__dept=dept