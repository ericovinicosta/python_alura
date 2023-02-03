def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'garrafa'
    acertou = False
    enforcou = False
    palavra = ['_' for letra in palavra_secreta]
    letras_erradas = []
  
    erros = 0

    print(palavra)
    while(not acertou and not enforcou):
        chute = str(input('Qual a letra desejada? ')).strip()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    palavra[index]=chute
                index += 1
        else:
            letras_erradas.append(chute)
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in palavra
        
        print('ERROS: {}'.format(letras_erradas))

        print(palavra)
        print('Jogando')

    if(acertou):
        print('Você ganhou!!')
    else:
        print('Você perdeu!! A palavra era {}'.format(palavra_secreta))

    print("Fim do jogo")
    
if(__name__=="__main__"):
    jogar()