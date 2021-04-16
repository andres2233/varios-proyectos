print('si respondes todo correcto te ganaras un dulce')
respuestasbien = 0
respuestasmal = 0

pregunta_1 = input('cual es mi nombre  \r\n')
if pregunta_1 == 'andres' :
    print('es correcto')
    print('ganaste un punto')
    respuestasbien += 1
    print(f'tienes {respuestasbien}')
else:
    print('estas equivocado master')
    respuestasmal += 1
    print(f'tienes {respuestasbien}')
pregunta_2 = input('donde vivo \r\n')
if pregunta_2 == 'elche':
    print('ganaste un punto')
    respuestasbien += 1
    print(f'tienes {respuestasbien}')
    
else:
    print('estas equivocado crack ')
  
    
pregunta_3 = input('que edad  tengo \r\n')
pregunta_3 = int(pregunta_3)
if pregunta_3 == 17:
    print('bien te sabes mi edad')
    respuestasbien += 1
    print(f'tieenes {respuestasbien} bien')
elif pregunta_3 < 17:
     print('tengo mas anos')
elif pregunta_3 > 17:
    print("tengo menos anos cruck ")

print (f'tus puntos totales son  {respuestasbien}')


    
