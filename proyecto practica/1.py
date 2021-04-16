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





numero()




