def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'
    acertou = False
    enforcou = False
    letras_certas = []

    for letra in palavra_secreta:
        letras_certas.append('_')

    while(not acertou and not enforcou):
        index = 0
        chute = str(input('Qual a letra desejada? ')).strip()
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_certas[index]=chute
            index += 1
        print(letras_certas)
        print('Jogando')

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()