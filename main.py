#Tabuada de um número usando loop while

import random

config = int(input('1 - [CONTINUAR] / 2 - [SAIR]: '))
num_sorted = random.randint(1, 20)

if config == 1:
    modo_de_jogo = int(input('1 - [FÁCIL] / 2 - [MÉDIO] / 3 - [DIFÍCIL]: '))

    if modo_de_jogo == 1:
        print('Modo de jogo: Fácil (40 tentativas)')
        tentativas = 40
        pontos = 0
    elif modo_de_jogo == 2:
        print('Modo de jogo: Médio (20 tentativas)')
        tentativas = 20
        pontos = 0
    elif modo_de_jogo == 3:
        print('Modo de jogo: Difícil (10 tentativas)')
        tentativas = 10
        pontos = 0

    while True:
        #Advinhe o número.
        numero = int(input('Advinhe o número: '))

        if numero == num_sorted:
            print('Você acertou!')
            tentativas += 3
            pontos += 3
            num_sorted = random.randint(1, 20)
            print('+3 tentivas')
            print(f'Pontos: {pontos}')

            if pontos == 50:
                print('Você venceu o jogo.')
                break
        elif numero != num_sorted:
            tentativas = tentativas - 1
            print(f'Restam {tentativas} tentativas.')

            if numero < num_sorted:
                print('É maior')
            else:
                print('É menor.')

        if tentativas == 0:
            print(f'Você perdeu. O número era {num_sorted}')
            break
    
elif config == 2:
    print('Você saiu do jogo.')