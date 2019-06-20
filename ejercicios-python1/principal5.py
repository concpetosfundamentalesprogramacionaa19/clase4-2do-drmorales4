"""
    @drmorales4
    Manejo de estructuras
"""
# Mi nombre es: Rene y mi Apellido es: Elizalde

diccionario = {"nombre": "René", "apellidos": "Elizalde"}
diccionario2 = {"nombre": "Luis", "apellidos": "Alvarez"}

lista: [diccionario, diccionario2]

print("Imprimir diccionario")

for l in lista:
	midiccionario = l
    print("Mi nombre es: %s y mi Apellido es: %s" % (midiccionario["nombre"], midiccionario["apellidos"]))


