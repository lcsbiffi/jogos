def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip() 

        index = 0 # Serve para guardar a posição da letra encontrada
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format (letra, index))
            index = index + 1    
        print("Jogando...")

    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()