#if anidados 
usuario_autentificado = True 
usuario_admin = True
if usuario_autentificado or usuario_admin:
    if usuario_admin:
        print('acceso permetido')
    else:
        print('acceso denegado')
else:

    print('denegado')
artrista = ';p;p'
print(f'holacomo estas {artrista}')


juegos = ['hola', 'lucas', 'juean']
#cambiar algo  de una lista
juegos[1]= 'paco'

print(juegos)
#eliminar algo de una lista
del juegos[2]
print(juegos)

# agregar objetos a un dicionario
estudiantes  = {}
estudiantes['nombres'] = 'hola mi gnte'
print(estudiantes)


for llave, valor in estudiantes.items(): #con el metodo items vamos a  saber las cosas que hay dentro
    print(valor) #hola mo gente 
    print(llave)# nombres 

#cuando hacemosun jeugos y el jugados pierde haemos algo asi 
# jugadores ={
#   'jugador': 'ándres',
#   'gol' : 1,
#   'gol_2':2, 
# }
# estudiantes['nombres'] = 'hola mi gnte'

# print(jugadores)
# del jugadores['nombre']
# print ('estudiantes')

#como hacer una pregunta
# nombre = input('ingresa tu nombre')
# print(f'bienvrenido{nombre}')

edad = 55
if edad >= 17:
    print ('tienes la edad neceesaria')

#para que sirve le comadno /r/n ?
#sirve para hacer un salto entre lineas 
 #edad = input ('cual es tu edad: \r\n')
#seria algo asi: 
# cual es tu edad : #salto
  #aqui ingraraias ti edad : 12

#como hacemos unacondicional con if y input d?
edad = input ('cual es tu edad: \r\n')
edad= int(edad) #necesario hacer este paso  y aque si no es program lo reconoce como un strin 'edad'
if edad >= 15 :
    print('te ganaste un chupiplpum ')


numero = input ('dime un numero y te dires si es par o no: \r\n')
numero= int( numero )
if numero % 2 == 0: #el signo % (llamado modulo) nos dice el sobrante de la kprecion y si no sobra nada es par 
    print(f'el nuemro {numero} es par ')
else:
    print(f'el numreo {numero} es impar')

