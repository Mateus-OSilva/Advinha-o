import forca
import adivinhacao

print("*********************************")
print("***Escolha o seu jogo***!")
print("*********************************")

print("(1) Forca (2) Advinhação)")

jogo = int(input("Qual o jogo?"))

if(jogo == 1):
    print("Jogando forca")
    jogar_forca()
elif(jogo == 2):
    print("Jogando advinhação")
    jogar_advinhacao()