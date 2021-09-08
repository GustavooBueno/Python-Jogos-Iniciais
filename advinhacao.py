import random

def jogar():

    print('======================================')
    print('   BEM VINDO AO JOGO DA ADVINHAÇÃO    ')
    print('======================================')
    print('')

    numero_secreto = round (random.randrange(1, 51))
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('[1] Fácil [2] Médio [3] Difícil\n ')


    nivel = int(input('Define um nível:' ))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else :
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input('Digite seu numero entre 1 e 50: '))

        if(chute < 1 or chute > 50):
            print('Voce deve digitar um número entre 1 e 50!')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print('Voce acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print("Voce errou, seu chute foi maior que o valor")
            elif(menor):
                print("Voce errou, seu chute foi menor que o valor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('\n===========')
    print('FIM DE JOGO')
    print('===========')

if (__name__ == '__main__'):
    jogar()