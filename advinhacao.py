import random

print('********************************')
print('Bem vindo ao jogo de Advinhação!')
print('********************************')

numero_secreto = round(random.random() * 100)
print('Selecione a dificuldade do Jogo')
print('1 - Fácil, 2 - Médio, 3 - Difícil')
nivel = int(input('Informe a dificuldade desejada: '))

while not(nivel in range(1,4)):
    print('O nível deve ser um valor de 1 a 3')
    nivel = input('Informe a dificuldade desejada: ')

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

pontos = 1000
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

    pontos_perdidos = abs(numero_secreto - chute)
    pontos -= pontos_perdidos

    rodada += 1
    ainda_joga = rodada <= total_de_tentativas

print('Fim de Jogo!!')