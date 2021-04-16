#vamos  a ver como se edita un contacto 

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
        opcion= input('\r\n seleccione una opcion: \r\n ')
        opcion= int(opcion) 
        if opcion ==1:
            agregar_contacto()
            
            preguntar = False
        elif opcion == 2:
            editar_contacto()
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

        
        

def editar_contacto():
    print('escribe el nombre del contacto a editar' )
    nombre_anterior = input('nombre del contacto que desea editar: \r\n')

    #revisar le archivo antes de editarlo 

    existe = existe_contacto(nombre_anterior )

    # aca revisamos que el archivo exista para pode rser modificado 
    if existe:
        print('puedes editar')
    else:
        print('ese contacto no existe')

def agregar_contacto():
    print ('desde agregar contacto()')
    nombre_contacto = input('nombre del contacto: \r\n ')

    
    existe = existe_contacto(nombre_anterior ) 
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
    
    app() 


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

#esto revisara si existe o no
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()