

def jogar():
    print("*********************************")
    print("***Bem vindo no jogo de Forca***!")
    print("*********************************")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("QUal letra? ")

        for letra in palavra_secreta:
            if(chute == letra):
                print(letra)

        print("Jogando...")
    
    
    print("FIm do jogo")

    

if (__name__ == "__main__"):
    jogar()
