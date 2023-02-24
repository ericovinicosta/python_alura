from random import random, randrange

def mensagem_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carregar_palavra_secreta():
    arquivo_de_palavra = open('palavra.txt', 'r')
    palavras_do_arquivo = []

    for linha in arquivo_de_palavra:
        palavras_do_arquivo.append(linha.strip())
    arquivo_de_palavra.close()

    index_segredo = randrange(0, len(palavras_do_arquivo))

    return palavras_do_arquivo[index_segredo]

def inicializa_palavra(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def pede_chute():
    return str(input('Qual a letra desejada? ')).strip()

def marca_chute_correto(chute, palavra_secreta, palavra):
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            palavra[index]=chute
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    mensagem_de_abertura()

    palavra_secreta =carregar_palavra_secreta()

    palavra = inicializa_palavra(palavra_secreta)

    acertou = False
    enforcou = False
    letras_erradas = []

    erros = 0

    print(palavra)
    while(not acertou and not enforcou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, palavra)
        else:
            letras_erradas.append(chute)
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in palavra

        print('ERROS: {}'.format(letras_erradas))

        print(palavra)
        print('Jogando')

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()

