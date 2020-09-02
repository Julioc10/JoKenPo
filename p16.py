from random import randint
from time import sleep

while True:

 itens = ('Pedra', 'Papel', 'Tesoura')

 computador = randint(0, 2)

 print('''\033[30m[ 1 ] Pedra
 [ 2 ] Papel
 [ 3 ] Tesoura\033[30m''')
 suae = int(input('Escolha uma opção:'))

 print('JÔ')
 sleep(1)

 print('KEN!')
 sleep(1)

 print('POO!!')
 sleep(1)

 if suae == 1:
    if computador == 0:
        print('\033[37mEmpate!')
    elif computador == 1:
        print('\033[36mVocê ganhou!')
    elif computador == 2:
        print('\033[33mO computador ganhou')

 elif suae == 2:
    if computador == 0:
        print('\033[36mVocê ganhou!')
    elif computador == 1:
        print('\033[37mEmpate!')
    elif computador == 2:
        print('\033[32mO computador ganhou!')

 elif suae == 3:
    if computador == 0:
        print('\033[36mVocê ganhou!')
    elif computador == 1:
        print('\033[32mO Computador ganhou!')
    elif computador == 2:
        print('\033[37mEmpate!')

 else:
        print('\033[31mNão tem essa opção! Tente dinovo\033[37m')
 print('Computador escolheu {}'.format(itens[computador]))
