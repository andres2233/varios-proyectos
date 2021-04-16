def app():
    inicio()
    pregunta = input('elige un numero:\r\n')
    pregunta = int(pregunta)
    while pregunta:
        if pregunta == 1: 
            opcion_1()
        elif pregunta ==2:
            opcion_2()
        elif pregunta == 3:
            numero()
            
            
    
                     
           
        

def opcion_1():
    print('\r\n HISTORIA CON DIFERENTES FINALES')
    print('jhon iva por la calle una noche caminado hacia su casa tristemente por que habia tenido un mal dia')
    print('paro un momento y miro una tienda de armas y le dieron ganas de acabar con esa mala vida \r\n')
    print('que hizo jhon?')
    print('1) entro a la tienda de armas para luego....')
    print('2) dejo ese pensamiento y siguio camindado a su casa ...')
    opciones = input('ingresa la opcion \r\n')
    opciones = int(opciones)
    while opciones:
        if opciones == 1:
            print('elegiste la opcion 1')
            print('jhon entra a la tienda y mira los precio, para su sopresa las armas son bastante barata ')
            print('entonces compra una revolver, el cual era una arma que le gustaba ya que veia muchas peliculas de vaqueros')
            print('iva camino a su casa recordando y pensando que dejaria de vivir y eso le daba un ppoco de miedo')
            opciones = False
        elif opciones == 2:
            print('elegiste la opcion 2')
            print('jhon siguio caminado a su casa.., cuando de repente un senora se le acerco y le dijo que si sabia donde estaba la: "la casa de los smith"')
            print('jhon sabia donde estaba, pero estaba pensando que seri mejor....')
            print('opciones')
            print('1) acompanarla hasta "la casa de los smith y distraerse un poco "')
            print('2) decirle donde quedaba he irse a su casa a hacer otras cosas')
            opciones = False

def opcion_2():
    insultos()


def insultos():
    inicio = ('\r\n escriba "insultos" para ver  los insultos que existen \r\n')
    inicio += 'escribe "cerrar" para dejar de llorar '
    inicio +='insultame y te devolvere el puto insulto \r\n '
    
    while inicio :
        list_insultos= input(inicio)
        if list_insultos == 'insultos':
            print('estos son los insultos existentes:')
            input('hola')
        elif list_insultos == 'cerrar':
            app()
        elif list_insultos == 'malparido':
            print('tonta')

def numero():
    numero = ('\r\n NUMERO PAR O INPAR\r\n')
    numero += 'escribe "cerrar" para salir a el menu principal\r\n' 
    numero += 'dime un numero y te dire si es par o no \r\n'
    while numero:
        respuesta = input(numero)
        
        if respuesta == 'cerrar':
            print('cerrando.....\r\n')
            app()
        else:
            respuesta = int(respuesta)
            if respuesta % 2 == 0 :
                print (f'el numero {respusta} es par')
            else:
                print(f'el numero {respuesta} no es par ')




    
   
    



def inicio():
    print('selelcione del menu lo que desea hacer:')
    print('1) historia con opciones ')
    print('2) insultos')
    print('3) te dire si un numero es par  o no ')
    
    
app()