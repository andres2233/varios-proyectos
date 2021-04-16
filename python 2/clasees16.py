#POLIMORFISMO 


class Restaurant: 
    def __init__(self,  nombre, categoria, precio): 
        self.nombre= nombre
        self.categoria = categoria
        self.precio = precio 
    
     #gater (obtine una valor ) y seters (cambia un valor) 

    def mostra_informacion(self):
        print(f'nombre: {self.nombre}, categoria:{self.categoria }, precio:{self.precio}') #
    def get_precio(self):
        print(self.precio)
    def set_precio(self, precio):
        self.precio= precio
    
    #HERENCIA
#crear una clase hijo  de Restaurant:

class Hotel(Restaurant): #la clase hotel hereda las funciones de Restaurant
    def __init__(self,  nombre, categoria, precio, alberca ):
        super().__init__(nombre, categoria, precio) #el super hace referencia a los atributos que vamos a heredar de la clase padre
        self.alberca = alberca #aca estamos creando un atributo nuevo para Hotel 
      
    #vamos a reescribir un metodo el cual esta en la clase padre( debe ser llamado igual al anterior )
    def mostra_informacion(self):
        print(f'nombre: {self.nombre}, categoria:{self.categoria }, precio:{self.precio}, alberca: {self.alberca}')

    #agreagr un metedo qu solo exista en hotel 
    def get_alberca(self):
        return self.alberca

hotel = Hotel('hotel poo', '5 estrellas', 200, 'si') #el si hace referencia a si hay o no alberca 
hotel.mostra_informacion()
alberca = hotel.get_alberca()
print(alberca)