#se importan las clases 
#ya que aprendiz importa la clase persona no es necesario importar esta 
from Aprendiz import *
from Curso import *

#se intancia objeto de aprendiz y se le agrega sus argumentos como nombre, documento, formacion y ficha 
objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629)
#print(objeto.__dict__)
#se instancia objcurso de la clase curso con el nombre del curso y su tipo
objcurso=Curso("Programacion Software","tecnico")
#se le agrega el curso a objeto mediante el metodo agregarXurso y se le pasa como parametro objCurso 
objeto.agregarCurso(objcurso)
#print(objeto.__dict__)
objeto.componerCurso()
objeto.componerCurso()
#print(objeto.verCursos())
#este for nos permite ver los nombres asignados a cada curso 
for cursito in objeto.verCursos():
    print(cursito.getNombre())


