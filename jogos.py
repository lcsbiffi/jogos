import forca
import adivinhacao

def escolhe_jogo():
    print("****************************")
    print("*******Escolha o jogo*******")
    print("****************************")

    print("(1) FORCA (2) ADIVINHAÇÃO")

    jogo = int(input("Escolha um jogo: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    else:
        print("Você precisa escolher entre 1 e 2.")

if (__name__ == "__main__"):
    escolhe_jogo()