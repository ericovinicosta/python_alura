def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'
    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        chute = str(input('Qual a letra desejada? ')).strip()
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(chute, end=' ')
            print('_', end='')
        print('')
        print('Jogando')

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()