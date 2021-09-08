import forca
import advinhacao

def escolheJogo():
    print('======================================')
    print('          ESCOLHA O SEU JOGO    ')
    print('======================================')
    print('')

    jogo = int (input ('[1] Advinhação  [2] Forca : '))

    if jogo == 1:
        print('O jogo advinhação foi escolhido\n')
        advinhacao.jogar()
    elif jogo == 2:
        print('O jogo forca foi escolhido\n')
        forca.jogar()

if (__name__ == '__main__'):
    escolheJogo()

