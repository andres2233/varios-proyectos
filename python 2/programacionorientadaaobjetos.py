#programaciion orientada a  objetos

class Restaurant: # esta es la clase
    def agregar_restaurnat(self, nombre): #aqui la funcio seria un metodo al estar dentro de una clase 
     #self toma como valor a agreagar_resaurant 
       
        print ('ágregando....')
        self.nombre= nombre #atributo 
        

    def mostra_informacion(self):
        print(f'nombre: {self.nombre}')
       

#instanciar la clase  
restaurant= Restaurant() # el primero vendria siendo un objeto( restaurann: el cual puede ser nombrado de cualquier manera) y Restaurant seria  la clase 
restaurant.agregar_restaurnat('pizeria1111111') #aqui el self no se pone ya que se pasa automaticamente 
restaurant.mostra_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurnat('KKKKKK') 
restaurant2.mostra_informacion()

#otra manera para mostrar la informacion 
print(f'nombre Restaurant: {restaurant.nombre}')
print(f'nombre Restaurant: {restaurant2.nombre}')
