import turtle
import time

posponer= 0.075

#configuracion de la pantalla de inicio 
frame = turtle.Screen()
frame.title('juego de culebrita creado por andres')
frame.bgcolor('black')
frame.setup(width = 600, height = 600)
frame.tracer(0)

#cabeza de culebra
cabeza= turtle.Turtle()
cabeza.speed(0) #desde este momento aparecera la cabeza de la tortuga 
cabeza.shape('square') #esto es la forma que va a tener la cabeza
cabeza.color('white')
cabeza.penup() # es par aque el movimiento de la serppierte no deje ragos o lineas 
cabeza.goto(0, 0) #the sake will star in the middle  
cabeza.direction = 'stop' #here the snake dont move until i do somethingd


def arriba(): 
    cabeza.direccion = 'up'


def abajo():
    cabeza.direccion = 'down'


def izquierda():
    cabeza.direccion = 'left'


def derecha():
    cabeza.direccion = 'right' 

#functions

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
        #Teclado


frame.listen()
frame.onkeypress(arriba,'w')
frame.onkeypress(abajo,'s')
frame.onkeypress(izquierda,'a')
frame.onkeypress(derecha,'d')

while True:
 frame.update() #funcion no precisa. hace un buvle en el que se repite la accion . 
mov()
time.sleep(posponer)





 
 #for x in range(100):s
    # ty.forward(x)
   # ty.left(90)
    