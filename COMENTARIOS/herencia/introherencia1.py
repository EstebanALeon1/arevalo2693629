#Se crea la superclase Vehicle
class Vehicle:
    pass

#Se crea la subclase LandVehicle que hereda de Vehicle 
class LandVehicle(Vehicle):
    pass

#Se crea la subclase TrackedVehicle que hereda de LandVehicle 
class TrackedVehicle(LandVehicle):
    pass
#print(issubclass(TrackedVehicle,(Vehicle,LandVehicle)))#se usa para verificar si una clase es una subclase 

#se crean objetos para cada clase
v=Vehicle()
lv=LandVehicle()
tv=TrackedVehicle()

#se crean bucles para iterar las clases y verificar a traves de la funcion isinstance si un objeto pertenece a una clase 
for cls1 in [v,lv,tv]:
      for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
          print(isinstance(cls1,cls2), end="\t")
      print()


# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#      for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#          print(issubclass(cls1, cls2), end="\t")
#      print()