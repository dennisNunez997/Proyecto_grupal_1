# Proyecto_grupal_1
primer trabajo grupal

#menu de figuras
#funciones
#funcion para calcular el volumen de un cubo
import math
def cubo(a, b, c):
	if (a == b) & (a == c):
		
		cubo = a*b*c
		return cubo
	else:
		return 0

def piramideTriangular(l,h):
	VolumenPiramide = (math.sqrt(3)*(l**2)*h)
	return VolumenPiramide

#*******MENU********
	 
ListaOpciones = {'a': 'a) cubo','b': 'b) piramide de base triangular','c': 'c) piramide de base cuadrangular','d': 'd) esfera' }
for i in ListaOpciones: 
    print(ListaOpciones[i])

Seleccion = input('seleccionar una de las opciones: ')

if Seleccion == 'a':
	print('\n Calcular el volumen de un cubo \n')
	a = int(input('ingrese la base: '))
	b = int(input('ingrese la altura: '))
	c = int(input('ingrese la profundidad: '))
	print('el volumen es: ')
	print(cubo(a,b,c))

elif Seleccion == 'b':
	print('\n piramide de base triangular \n')
	l = int(input('ingrese el lado: '))
	h = int(input('ingrese la altura: '))
	print('el volumen es: ')
	print(piramideTriangular(l,h))

elif Seleccion == 'c':
	print('piramide de base triangular')

elif Seleccion == 'd':
	print('esfera')
    #El volumen de una esfera
import math
radio_esfera = float(input("Ingrese el radio de la esfera: "))
volumen_esfera = (4/3)*(math.pi)*(radio_esfera**3)
print("El volumen de la esfera es: ",volumen_esfera,"m³")

else:
	print('esta opcion no esta definida')

