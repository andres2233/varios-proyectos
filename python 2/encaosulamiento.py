class Restaurant: # esta es la clase
    def __init__(self,  nombre, categoria, precio): #contructor
        self.nombre= nombre
        self.categoria = categoria
        self._precio = precio 
    
     

    def mostra_informacion(self):
        print(f'nombre: {self.nombre}, categoria:{self.categoria }, precio:{self._precio}') #ABSTRACION
        #utilizado cuando es un private 
    def get_precio(self):
        print(self._precio)
    def set_precio(self, precio):
        self._precio= PRECIO

#instanciar la clase  
restaurant =  Restaurant('pizeria', 'comida rica', 20)
print(restaurant._precio)
restaurant._precio = 80#no sera posibla modificar el valor de 20 con este metodo
#restaurant.get_precio() #asi savemos el precio de un private 
restaurant.mostra_informacion()

restaurant2 = Restaurant('comida freca ', 'comida de casa', 50)
print(restaurant2._precio)
restaurant2._precio = 40
restaurant2.mostra_informacion()
restaurant2.get_precio()


 #SET 
class Restaurant: # esta es la clase
    def __init__(self,  nombre, categoria, precio): #contructor
        self.nombre= nombre
        self.categoria = categoria
        self.__precio = precio 
    
     

    def mostra_informacion(self):
        print(f'nombre: {self.nombre}, categoria:{self.categoria }, precio:{self.__precio}') #ABSTRACION
    def get_precio(self):
        print(self.__precio)
    # otra manera de aplicar get es:
    # def get_precio(self):
    #     return self.__precio
       #para inprentar  el valor seria algo asi:
     #precio = restaurant.get_precio  
    def set_precio(self, precio):
        self.__precio= precio

#instanciar la clase  
restaurant =  Restaurant('pizeria', 'comida rica', 50)
#print(restaurant.__precio)
#restaurant.__precio = 80#no sera posibla modificar el valor de 50 con este metodo
restaurant.get_precio() #asi savemos el precio de un private 
restaurant.set_precio(80)
restaurant.mostra_informacion()


restaurant2 = Restaurant('comida freca ', 'comida de casa',40)
#print(restaurant2.__precio)
#restaurant2.__precio = 40
restaurant2.mostra_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()

