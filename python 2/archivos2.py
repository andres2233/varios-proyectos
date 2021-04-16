def app():
    #crear archivo
    with open('archivo.txt') as archivo: # as es como crear un alias a archivo.txt
        for contenido in archivo:
            print(contenido.rstrip()) #la metodo rstrip sirve para que no deje espacios entre los textos, para entender mejor puevalo con y sin el metodo




    


app()