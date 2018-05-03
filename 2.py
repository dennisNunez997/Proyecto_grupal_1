#calculadora

def invertirCadena(cadena):
    #se crea una variable que para ingresar el valor
    cadena = input('ingrese la cadena: ')
    #se crea otra variable para llamar saber el tamaño de la cadena
    valor = len(cadena)
    #se crea un bucle usando la variable anterior, para que actue como contador, y que este inicie desde la ultima posicion
    for valor in cadena:
        print(int(valor))
        valor = valor-1
    
def creartxt():
    archivo = open('2.txt','w')
    archivo.close()
#creartxt()

def escribirtxt():
    archivo = open('2.txt','a')
    print("cadena invertida")
    cadena = input('ingrese la cadena: ')
    
    archivo.write(invertirCadena(cadena))
    archivo.close()
    
def leertxt():
    archivo = open('2.txt','w')
    linea = archivo.readline()
    while linea != '':
        print(linea)
        linea = archivo.readline()
        archivo.close()
        
#def escribirtxt()
#def leertxt()