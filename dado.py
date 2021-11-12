from random import randint
from time import sleep

def espera():
    for c in range(0, 3):
        print('.', end='')
        sleep(1.5)

def linha():
    print('\33[34m-\33[m' * 40)

def titulo(msg):
    print('\33[35m=\33[m' * 40)
    print(f'\33[36m{msg.center(40)}\33[m')
    print('\33[35m=\33[m' * 40)

resultados = []

titulo('JOGO DO DADO')
while True:
    valor = randint(1, 6)
    resultados.append(valor)
    print(f'O valor do dado foi', end='')
    espera()
    print(f' \33[31m{valor}\33[m')
    sleep(1.5)
    rest = ' '
    while rest not in 'SN':
        try:
            rest = str(input('Deseja jogar o dado novamente? [S/N] ')).strip().upper()[0]
        except:
            print('Digite uma opção válida.')
    if rest == 'N':
        break
    linha()
linha()
for pos, valores in enumerate(resultados):
    print(f'{pos + 1}º valor: \33[31m{valores}\33[m')
    sleep(1)
linha()
print('Obrigado por jogar! Volte sempre.')
           