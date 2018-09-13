# coding=utf-8
import string

def qteste_zero(fita, pos, x): 
    print(len(x))
    fita[pos] = x[0] 
    novoX = x[1:] #passa o valor X sem o ultimo valor que foi para a fita
    print(len(novoX))

    if fita[pos] == ">":
        print("\n\nQSIM\n\n") 

    elif fita[pos] == "0":
        fita[pos] = ":" 
        pos -=1
        q_(fita, pos, novoX)
    elif fita[pos] == "1":
        print("\n\nQNAO\n\n") 
    

def qli_zero(fita, pos, x): #testar
    print(len(x))
    fita[pos] = x[0] 
    novoX = x[1:] #passa o valor X sem o ultimo valor que foi para a fita
    print(len(novoX))

    if fita[pos] == "0": 
        pos +=1
        qli_zero(fita, pos, novoX)
    elif fita[pos] == "1":
        pos +=1
        qli_zero(fita, pos, novoX)
    elif fita[pos] == ":":
        pos -=1
        qteste_zero(fita, pos, novoX)

def q_(fita, pos, x): #testar
    print(len(x))
    fita[pos] = x[0] 
    novoX = x[1:] #passa o valor X sem o ultimo valor que foi para a fita
    print(len(novoX))
    
    if fita[pos] == ">":
        pos +=1
        q0(fita, pos, novoX)
    elif fita[pos] == "0": 
        pos -=1
        q_(fita, pos, novoX)
    elif fita[pos] == "1":
        pos -=1
        q_(fita, pos, novoX)
    

def qteste_um(fita, pos, x):#testar
    print(len(x))
    fita[pos] = x[0] 
    novoX = x[1:] #passa o valor X sem o ultimo valor que foi para a fita
    print(len(novoX))

    if fita[pos] == ">":
        print("\n\nQSIM\n\n")

    elif fita[pos] == "0":
        print("\n\nQNAO\n\n")
    elif fita[pos] == "1":
        fita[pos] = ":"
        pos -=1
        q_(fita, pos, novoX)

def qli_um(fita, pos, x): #testar
    print(len(x))
    fita[pos] = x[0] 
    novoX = x[1:] #passa o valor X sem o ultimo valor que foi para a fita
    print(len(novoX))

    if fita[pos] == "0":
        pos +=1
        qli_um(fita, pos, novoX)
    elif fita[pos] == "1":
        pos +=1
        qli_um(fita, pos, novoX)
    elif fita[pos] == ":":
        pos -=1
        qteste_um(fita, pos, novoX)

def q0(fita, pos, x): #testar
    print(len(x))
    fita[pos] = x[0] 
    novoX = x[1:] #passa o valor X sem o ultimo valor que foi para a fita
    print(len(novoX))
    if fita[pos] == ">":
        pos +=1
        q0(fita, pos, novoX)
    elif fita[pos] == "0":
        fita[pos] = ">"
        pos +=1
        qli_zero(fita, pos, novoX)
    elif fita[pos] == "1":
        fita[pos] = ">"
        pos +=1
        qli_um(fita, pos, novoX)
    elif fita[pos] == ":":
        print("\n\nQSIM\n\n")
        
    
def main():
    fita = [":" for x in range(50)]
    fita[0] = ">" #marca o inicio
    
    x = input("Entre com a cadeia binaria: ")
    list(x) 

    if (x.isnumeric()) != True: #verifica se nao é vazio e se são numeros
        main()
    else:
        q0(fita, 1, x) #fita, posição da cabeça e valor de entrada

    
if __name__ == "__main__":
    main()  