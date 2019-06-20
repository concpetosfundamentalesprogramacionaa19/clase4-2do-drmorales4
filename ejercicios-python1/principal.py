"""
    @drmorales4
    Ejemplo de manejo de paquetes
"""
# para crear paquetes en python debemos crear un archivo "__init__.py"

# valor 2 elevado a la potencia es igual a 4
import math
from paquete1.informacion import valores
from paquete1.informacion2 import hacer_potencia


for l in valores:
	r = hacer_potencia(l, 2)
	print("valor %d elevado a la potencia %d es igual a %.2f" % (l, 2, r))
