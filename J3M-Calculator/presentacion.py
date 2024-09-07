class persona:
    def __init__(self,nombre,carrera,años,gustos):
        self.nombre = nombre
        self.carrera = carrera
        self.años = años
        self.gustos = gustos
        
    def presentacion(self):
        print(f"mi nombre es {self.nombre}\ntengo {self.años}\nestudio {self.carrera}") 
    
    def hoobies(self):
        print(f"Mi hoobie favorito es {self.gustos} y jugar futbol")
    
yo= persona("Marcos Valera","Ing.Sistemas",18,"escuchar musica")

print("Elige una opcion")
print("1.presentacion\n2.Hoobies")


while True:
    a=int(input(">>>"))
    if a==1:
        yo.presentacion()
    elif a==2:
        yo.hoobies()
    else:
        print("Numero erroneo")
        