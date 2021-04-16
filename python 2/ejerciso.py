playlist = {} #dicionario vacio 
playlist['canciones'] =[] #lista vacia de canciones que se va lleando con las respuestas



#funcion principal

def app():
     #agreagr play list:
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('como deseas nombrar  la play list \r\n ' )
        if nombre_playlist:
            playlist['nombre']= nombre_playlist
            #ya tenemos un nombre desactivar el true
            agregar_playlist = False
            print (playlist)
            #mandar a llamar la funcion  para agregar canciones  
            agregar_cancion()
        else:
            print('no se pudo  crear el programa ')
            agregar_playlist = False
      
def agregar_cancion():
    
    agregar_cancion = True
    while agregar_cancion:
        kaka = playlist ['nombre']
        pregunta = f'\r\n agreagar canciones para la play list {kaka}: \r\n'
        pregunta +='escribe "x" para dejar de agreagr canciones \r\n '
        
        cancion  = input(pregunta)
        if cancion == 'x':
            #dejar de agreagr canciones
            print('finalizando....')
            agregar_cancion = False # con este detenemos la ejecucion de l programa 

            #mostar resumen de la playlist que hicimos 
            mostar_resumen()
        else:
            #agregar  las canciones a la playlist
            playlist['canciones'].append(cancion) #el metodo append sirve para agregar 
            print(playlist)

def mostar_resumen():
    
    nombre_playlist = playlist['nombre']
    print(f'musica en play list : {nombre_playlist} \r\n')
    print('canciones: ')
    for cancion in playlist['canciones']:
        print(cancion)

app()