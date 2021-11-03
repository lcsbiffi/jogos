def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    acertou = False
    enforcou = False

    print(letras_acertadas)

    while(not acertou and not enforcou):
        chute = input("Qual a letra? ")
        chute = chute.strip() 

        index = 0 # Serve para guardar a posição da letra encontrada
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra # Como já temos o índice da letra, basta substituir naquela posição do array pela letra que acertamos.
            index = index + 1 
        print(letras_acertadas)   

    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()