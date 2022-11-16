

def jogar():
    print("*********************************")
    print("***Bem vindo no jogo de Forca***!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1

        else:
            erros += 1
        
        enforcou = erros == 6

        print(letras_acertadas)
    
    
    print("FIm do jogo")

    

if (__name__ == "__main__"):
    jogar()
