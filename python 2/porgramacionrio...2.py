 #programaciion orientada a  objetos

class Restaurant: # esta es la clase
    def __init__(self,  nombre): #contructor. con el cual se puede evitar utilizar lo de lapractica de programacionoreintadaaobjetos.py
        self.nombre= nombre 

    def mostra_informacion(self):
        print(f'nombre: {self.nombre}')

 #instanciar la clase  
restaurant = Restaurant('pizeria1111111') # al pasarlo a la clase pasa a ser constructor , necesario ver la practica pasada para entedner
restaurant.mostra_informacion()

restaurant2 = Restaurant('KKKKKK')
restaurant2.mostra_informacion()

 # EJEMPLO 2 
class Restaurant: # esta es la clase
    def __init__(self,  nombre, categoria): #contructor
        self.nombre= nombre
        self.categoria = categoria
    
     

    def mostra_informacion(self):
         print(f'nombre: {self.nombre}, categoria:{self.categoria }') #se agrega a categaoria como metodo para 
         #que sea detectada ppor self del contario no la imprimira 

 #instanciar la clase  
restaurant = Restaurant('pizeria1111111', 'comida francesa') # al pasarlo a la clase pasa a ser constructor 
restaurant.mostra_informacion()

restaurant2 = Restaurant('comida freca ', 'comida de casa')
restaurant2.mostra_informacion()

# ejemplo 3 
class Restaurant: # esta es la clase
    def __init__(self,  nombre, categoria, precio): #contructor
        self.nombre= nombre
        self.categoria = categoria
        self.precio = precio 
    
     

    def mostra_informacion(self):
        print(f'nombre: {self.nombre}, categoria:{self.categoria }, precio:{self.precio}') #ABSTRACION

#instanciar la clase  
restaurant = Restaurant('pizeria', 'comida rica', 20)
restaurant.mostra_informacion()

restaurant2 = Restaurant('comida freca ', 'comida de casa', 50)
restaurant2.mostra_informacion()