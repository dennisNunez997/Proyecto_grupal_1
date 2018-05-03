#calculadora

def calculadora(numero):
    #crea una variable de entrada
    #luego se recorre la cadena mediante un for
    #el cual usara una variable local para ubicar las posiciones de cada numero convertido en str
    for valor in numero:
        #se añade un incremento para el exponente.
        i=i+1
        #se añade una operacion para la multiplicacion del entero junto con la potencia.
        potencia = math.pow(2,i)
        #se multiplica el valor con la potencia.
        valor = valor * 2*potencia
        #se imprime
        print(int(valor))
    
    
def creartxt():
    archivo = open('1.txt','w')
    archivo.close()
creartxt()

def escribirtxt():
    archivo = open('1.txt','a')
    print("calculadora")
    numero = input('ingrese el numero binario: ')
    
    archivo.write(str(calculadora(numero)))
    archivo.close()
    
def leertxt():
    archivo = open('1.txt','w')
    linea = archivo.readline()
    while linea != '':
        print(linea)
        linea = archivo.readline()
        archivo.close()
        
    
#escribirtxt()
#leertxt()