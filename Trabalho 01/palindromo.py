# coding=utf-8
import string

def qteste_zero(fita, pos): #pronto
    if fita[pos] == ">":
        print("\n\nQSIM\n\n") 

    elif fita[pos] == "0":
        fita[pos] = ":" 
        pos -=1
        q_(fita, pos)
    elif fita[pos] == "1":
        print("\n\nQNAO\n\n") 
    
def qli_zero(fita, pos): #pronto
    if fita[pos] == "0": 
        pos +=1
        qli_zero(fita, pos)
    elif fita[pos] == "1":
        pos +=1
        qli_zero(fita, pos)
    elif fita[pos] == ":":
        pos -=1
        qteste_zero(fita, pos)

def q_(fita, pos): #pronto  
    if fita[pos] == ">":
        pos +=1
        q0(fita, pos)
    elif fita[pos] == "0": 
        pos -=1
        q_(fita, pos)
    elif fita[pos] == "1":
        pos -=1
        q_(fita, pos)

def qteste_um(fita, pos): #pronto
    if fita[pos] == ">":
        print("\n\nQSIM\n\n")

    elif fita[pos] == "0":
        print("\n\nQNAO\n\n")
    elif fita[pos] == "1":
        fita[pos] = ":"
        pos -=1
        q_(fita, pos)

def qli_um(fita, pos): #pronto
    if fita[pos] == "0":
        pos +=1
        qli_um(fita, pos)
    elif fita[pos] == "1":
        pos +=1
        qli_um(fita, pos)
    elif fita[pos] == ":":
        pos -=1
        qteste_um(fita, pos)

def q0(fita, pos): #pronto
    if fita[pos] == ">":
        pos +=1
        q0(fita, pos)
    elif fita[pos] == "0":
        fita[pos] = ">"
        pos +=1
        qli_zero(fita, pos)
    elif fita[pos] == "1":
        fita[pos] = ">"
        pos +=1
        qli_um(fita, pos)
    elif fita[pos] == ":":
        print("\n\nQSIM\n\n")

def invalido(x): #verifica se é somente 0 e 1
    carac = "23456789"
    i = 0
    while i < len(x):
        if (x[i] in carac) == True:
            return True
        i += 1 
    return False

def main():
    fita = [":" for x in range(50)] #preenche a fita com o simbolo de final -> (:) 
    fita[0] = ">" #marca o inicio
    
    x = input("Entre com a cadeia binaria: ")

    if (x.isnumeric()) != True: #verifica se nao é vazio e se são numeros
        main()
    elif (invalido(x)) == True:
        main()
    else:
        indice = 0
        pos = 1
        #coloca a cadeia binaria na fita
        while indice <len(x):
            fita[pos] = x[indice]
            pos += 1
            indice += 1
        
        #print(fita)
        #primeira chamada de função para verificar
        q0(fita, 1) #fita, posição da cabeça e valor de entrada

if __name__ == "__main__":
    main()  