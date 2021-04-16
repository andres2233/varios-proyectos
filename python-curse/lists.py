 #vamos a  ver como hacaer una lista de objetos en python
#demo_list=["HOLA", GREEN, [2, 3, 4], TRUE]
  #como se hace unalista de numeros 
number_list = list((1, 2, 3, 4))
print(number_list)
print(type(number_list)) #ype es para saber que tipo de string es 

#Con este cpmado hacemos una lista de un numero a otro o rango 
entre = list(range(1, 200)) #el valor siempr llega un numero menos osea 1 a 199
print(entre)
# para saber las fuciones que se pueden hacer en una lista
colors = ["green", "black", "yelow"]
print(dir(colors))
#para saber la cantidad de cofuncionesque se pueden hacer en una lista 
print(len(colors))
#para saber si algo esta o no dentro de una lista aplicamos el comando :
print("green" in colors)
#la respuesta sera true si si esta o false si no lo esta esto es llamado boolean

#si quieres cambair algo de una list si cambiarlo directamente enotneces :
colors["green"]= "blackplatano"
print(colors)
#si quieres agreagr varios srings a una lista se utiliza el siguiente comando 
colors.extend(["violet", "purple"])
print(colors)
#para poner un strin en una posicion espesifica :
colors.insert(1, "papaya" )