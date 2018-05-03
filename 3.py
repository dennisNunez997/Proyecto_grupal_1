#codificador

def codificador(mensaje):
    #se almacena una lista de numeros
    listaA = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22"
    #se implementa la lista de numeros en la lista de palabras
    listaB = "T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E"
    #se crea un bucle, el cual usara el contador para ubicar la posicion de cada letra dentro del mensaje
    #y se llama a la funcion "find", la cual buscara cada letra que la variable "valor", haya buscado
    #y la cual la ira relacionando, con el lista de los numeros.
    for valor in mensaje:
        print(listaA.find(valor))
    
    
def creartxt():
    archivo = open('3.txt','w')
    archivo.close()
#creartxt()

def escribirtxt():
    archivo = open('3.txt','a')
    print("codificador")
    mensaje = input('ingrese el mensaje: ')
    codificador(mensaje)
    archivo.write(codificador(mensaje))
    archivo.close()
    
def leertxt():
    archivo = open('3.txt','w')
    linea = archivo.readline()
    while linea != '':
        print(linea)
        linea = archivo.readline()
        archivo.close()
        
#escribirtxt()
#leertxt()