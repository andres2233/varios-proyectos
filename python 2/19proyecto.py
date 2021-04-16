import os # importamos una funcion de el codigo de python que sirve para manejar archivos 
CARPETA = 'contactos/'#cuando escribimos en  mayuscula lgo da a entender que es una constante y que no se dabe de modificar el valor 
EXTENSION = '.txt' #extenion de archivos 

#contactos 
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono 
        self.categoria = categoria 




def app():
    #resvisa si la carpeta existe o no.
    crear_directorio()
    #muestra el  menu de opciones 
    mostrar_menu()
    #preguntar a el ususario la opcion a usar 

    preguntar = True
    while preguntar:
        opcion= input('seleccione una opcion: \r\n ')
        opcion= int(opcion) #cambia el el strina un numero 
        #ejecutar opciones
        if opcion ==1:
            agregar_contacto()
            #print('agreagar contacto')
            preguntar = False
        elif opcion == 2:
            editar_contacto()
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
    #resivisa si el archivo ya existe antes de crealo 
    existe  = existe_contacto(nombre_anterior)
    if not existe: 
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo: # lo que hace extencio es convertir el archivo a .txt que esto es texto , el w representa dar permiso a que se pueada escribir
            #resto de los campos
            telefono_contacto = input('agregra el telfono:\r\n')
            categoria_contacto = input('categoria contacto: \r\n')
            #instacia la clase:
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            #escribir en el archivo 
            archivo.write('nombre:' + contacto.nombre + '\r\n') # esto lo que hace es escribi el nombre de el contacto
            archivo.write('telefono:' + contacto.telefono + '\r\n') # el nombre (contacto) es el nombre de el objeto , lo tenomos en la linea 54
            #y el .telefono vendria siendo el atributo de la calse la cual tenemos en la linea 9
            archivo.write('categoria :' + contacto.categoria + '\r\n') 
            
            #mostrar mensaje de exito ( osea que todo ha salido bien )
            print('\r\n contacto creado correctamente \r\n')

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

def editar_contacto():
    print("escribe el nombre de el contacto a editar ")
    nombre_anterior = input('nombre de el contacto que desea editar \r\n')
    #resivisa si el archivo ya existe antes de editarlo
    existe  = existe_contacto(nombre_anterior)
    if existe:
        print('puedes editar ')
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('agrega el nuevo nombre : \r\n ')
            telefono_contacto = input('agregra el nuevo telfono:\r\n')
            categoria_contacto = input('categoria la nueva categoria : \r\n')
             
             #intanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            #escribir en el archivo

            archivo.write('nombre:' + contacto.nombre + '\r\n') 
            archivo.write('telefono:' + contacto.telefono + '\r\n') 
            archivo.write('categoria :' + contacto.categoria + '\r\n') 
            
            #renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            #mostar un mensaje de que los cambios salieron bien :
            print('\r\n contacto editado correctamente ')

    else:
        print('ese contacto no existe ')

#esto va a revisar si existe o no el contacto 
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()