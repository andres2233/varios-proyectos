import turtle
import time
import random #este es para la comida

posponer = 0.075

#configuracion de la pantalla de inicio 
frame = turtle.Screen()
frame.title('Juego de la culebrita hecho por andresillo')
frame.bgcolor('black')
frame.setup(width=600, height=600)
frame.tracer(0)

# Cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0) #este comando es necesario para que se mueva latortuga o si no se quedara ainmovil
cabeza.shape('square')#esto es la forma que va a tener la cabeza
cabeza.color('white')
cabeza.penup()#  penup hace que el movimiento de la serppierte no deje ragos o lineas 
cabeza.goto(0, 0)#the snake will start in the middle  
cabeza.direccion = 'stop' #here the snake dont move until i do something


# Funciones que van a cambiar de direccion
def arriba():
    cabeza.direccion = 'up'


def abajo():
    cabeza.direccion = 'down'


def izquierda():
    cabeza.direccion = 'left'


def derecha():
    cabeza.direccion = 'right'


#  Funcion del movimiento
def mov():
    if cabeza.direccion == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    elif cabeza.direccion == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    elif cabeza.direccion == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    elif cabeza.direccion == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)


# Teclado
frame.listen()
frame.onkeypress(arriba, 'w')
frame.onkeypress(abajo, 's')
frame.onkeypress(izquierda, 'a')
frame.onkeypress(derecha, 'd')

#cuerpo serpite
segmentos = [] #asi creamos una lista vacia la cual va a air creciendo cuando comamos puntitos 

 #comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0, 100)
segmentos = []
# Creo un bucle que va a correr durante el juego
# Se llama bucle principal
while True:
    frame.update() #funcion no precisa. hace un buvle en el que se repite la accion .
    mov()
    time.sleep(posponer)
    #colicion de la comida
    if cabeza.distance(comida) <20: #el 20 es para la distacia que tiene que estar la culebra para que se como la comida , hay que re
        #cordar que un pixel mide 20 por es otodo pixel mayor a 20 seracomido
      x=  random.randint(-280, 280) #despues de haber comido , la comida aparecera en un rango de 280 pixeles aunque tengamos 300
      y=  random.randint(-280, 280)# no usamos los 300 o la comida apareceria afuera
      #randit se ignifica random intenger .
      comida.goto(x,y)

       #crear cuerpo de serpierte a medida que come puntos
      nuevo_segmento = turtle.Turtle()
      nuevo_segmento.speed(0)
      nuevo_segmento.shape('square')
      nuevo_segmento.color('grey')
      nuevo_segmento.penup()
      segmento.append(nuevo_segmento) #cada vez que se crea un nueva vola se agreag a la serpiente
    #mover el cuerpo de la serpiernte 
    totalSeg = len(segmentos)# con el comando len estamos preguntando cuantas cosa hay en una lista   
    for index in range(totalSeg -1, 0, -1):
        x = segmento[ index -1].xcor()
        y = segmento[index -1].ycor()
        segmento[index].goto(x,y) #goto hace que se mueva  ha esa cordenadas 

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmento[0].goto(x,y)     