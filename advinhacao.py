import random

print('********************************')
print('Bem vindo ao jogo de Advinhação!')
print('********************************')

numero_secreto = round(random.random() * 100)
total_de_tentativas = 3
rodada = 1
ainda_joga = rodada < total_de_tentativas

while(ainda_joga):
    print('Tentativa {} de {}:'.format(rodada, total_de_tentativas))
    str_chute = input('Digite seu número: ')
    print('Você digitou ', str_chute)
    chute = int(str_chute)

    acertou = numero_secreto == chute
    maior = numero_secreto < chute
    menor = numero_secreto > chute

    if(acertou):
        print('Você acertou!!')
        break
    else:
        print('Você errou!', end=" ")
        if(menor):
            print('O seu Chute foi menor que o Segredo!')
        elif(maior):
            print('O seu Chute foi maior que o Segredo!')

    rodada += 1
    ainda_joga = rodada <= total_de_tentativas

print('Fim de Jogo!!')