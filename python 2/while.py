pregunta = ('escribe "cerrar" para salir de la aplicacion \r\n')
pregunta +=  'dime un numero y te dires si es par o no: \r\n'
#preguntar = True

while pregunta: #while solo se ejecuta solo  si es true y ciando es false se cambiatodo 

    numero = input (pregunta)
    if numero == 'cerrar':
        pregunta= False
    else:

        numero= int(numero)


        if numero % 2 == 0: #el signo % (llamado modulo) nos dice el sobrante de la kprecion y si no sobra nada es par 
            print(f'el nuemro {numero} es par ')
        else:
            print(f'el numreo {numero} es impar')
                                                          

#otro ejemplo 
#errores en whiles
numero = 0
# while numero <= 10 :
#     print(numero) #aqui esata el error,si no le ponemos la suma a el numero while se ejecutara infinito
#     numero += 1 # aqui estas usma hace que while sea false ya que numero es igual a 11

#if denttro del while 
while numero <= 10 :
    if numero == 5:
        print('cincooooooo')
        break # detiene la ejecucion cuando se detiene
    else:
        print(numero)
    numero += 1