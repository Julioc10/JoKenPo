num = int(input('Digite um número:'))
print('''Conversoes
[ 1 ] Binario
[ 2 ] Octal
[ 3 ] Hexadecimal''')
op = int(input('Escolha uma das opções:'))
if op == 1:
    print(f'Seu número em binário é {bin(num)[2:]} ')
elif op == 2:
    print(f'Seu número em Octal é {oct(num)[2:]}')
elif op == 3:
    print(f'Seu número em Hexadecimal é {hex(num)[2:]}')
else:
    print('\033[31mVocê não digitou a opção certa!\033[37m')
