def app():
    #crear archivo
    archivo = open('archivo.txt', 'w') #open es una funcion ,archivo.txt esun archivo que creamos, w es permiso  de escritura dentro del archivo.txt 
   # si el archivo no esxiste lo crea automaticamete
    #generar numeros en archivo 
    for i in range(0, 50):# i es conocido como indice o incrememnto 
        archivo.write('esta es la linea ' + str(i) + '\r\n') # el i seria un entero , por lo cual lo convertimos a string para que pueda ser leido 

   #cerrar un archivo
    archivo.close()       




app()