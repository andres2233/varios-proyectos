# vamos a hacer un cambio para en caso que queramos crear dos contactos con el mismo nombre

import os
CARPETA = 'contactos/'
EXTENSION = '.txt' 

#contactos 
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono 
        self.categoria = categoria 




def app():
    
    crear_directorio()
     
    mostrar_menu()
    

    preguntar = True
    while preguntar:
        opcion= input('seleccione una opcion: \r\n ')
        opcion= int(opcion) 
        if opcion ==1:
            agregar_contacto()
            
            preguntar = False
        elif opcion == 2:
            print('editar contacto')
            preguntar =False
        elif opcion ==3 :
            print('ver contacto ')
            preguntar =False
        elif opcion == 4:
            print('buscar contacto')
            preguntar =False
        elif opcion ==5:
            print('eliminar contacto')
            preguntar =False
        else:
            print('opcion no valida, intente de nuevo ')
        
        


def agregar_contacto():
    print ('desde agregar contacto()')
    nombre_contacto = input('nombre del contacto: \r\n ')

    #revisar si el archivo ya existe y asi escribir dos con el mismo nombre.
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION) # isfile revisara si un archivo existe previamente 
    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo: 
            telefono_contacto = input('agregra el telfono:\r\n')
            categoria_contacto = input('categoria contacto: \r\n')
        
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
       
            archivo.write('nombre:' + contacto.nombre + '\r\n')
            archivo.write('telefono:' + contacto.telefono + '\r\n')
            archivo.write('categoria :' + contacto.categoria + '\r\n') 
        
       
            print('\r\n contacto creado correctamente \r\n')
    else:
        print(f'\r\n el contacto: {nombre_contacto} ya existe \r\n')
    #reiniciar la app 
    app() # tenemos que poner esto para que en caso de que ya exista un contacto con ese nombre osea else se vuelva a abrir la app hasta que pongamos uno que no exista 


    


def mostrar_menu():
    print('selelcione del menu lo que desea hacer:')
    print('1) agregar nuevo contacto')
    print('2) editar un contacto  ')
    print('3) ver contactos ')
    print('4) buscar contacto ')
    print('5) eliminar contacto')
    
def crear_directorio():
    if not os.path.exists(CARPETA):  
        os.makedirs(CARPETA) 
    else:
        print(f'\r\n la carpeta: {CARPETA} fue creada anteriormente  \r\n')


app()
