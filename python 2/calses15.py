class Restaurant: # esta es la clase
    def __init__(self,  nombre, categoria, precio): #contructor
        self.nombre= nombre # atributo
        self.categoria = categoria
        self.__precio = precio 
    
     #gater (obtine una valor ) y seters (cambia un valor) 

    def mostra_informacion(self):
        print(f'nombre: {self.nombre}, categoria:{self.categoria }, precio:{self.__precio}') #ABSTRACION
    def get_precio(self):
        print(self.__precio)
    def set_precio(self, precio):
        self.__precio= precio
    
    #HERENCIA
#crear una clase hijo  de Restaurant:

class Hotel(Restaurant): #la clase hotel hereda las funciones de Restaurant
    def __init__(self,  nombre, categoria, precio):
        super().__init__(nombre, categoria, precio) #el super hace referencia a la clase padre

hotel = Hotel('hotel poo', '5 estrellas', 200)
hotel.mostra_informacion()