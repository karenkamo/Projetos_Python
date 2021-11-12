from random import choice
from time import sleep

cores = {'limpa': '\33[m',
         'vermelho': '\33[31m',
         'verde': '\33[32m',
         'amarelo': '\33[33m',
         'azul': '\33[34m',
         'magenta': '\33[35m',
         'ciano': '\33[36m',
         'cinza': '\33[37m',
         'amarelofundo': '\33[1;43m'}

def titulo(msg):
    print('\33[36m=~\33[m' * 25)
    print(f'{cores["azul"]}{msg.center(50)}{cores["limpa"]}')
    print('\33[36m=~\33[m' * 25)
    
def linha():
    print('\33[34m-\33[m' * 50)
    
def escolha_computador(lista):
    valor = choice(lista)
    return valor

def mostrar(variavel):
    print(f'Eu escolhi', end='')
    for c in range(0, 3):
        print('.', end='')
        sleep(1)
    print(f'{cores["cinza"]}{variavel}{cores["limpa"]}')

def temporizador(msg):
     print(msg, end='') 
     for c in range(0, 3):
         print('.', end='')
         sleep(0.5)
     
def jogo(lista):
    global jogador, computador
    juntos = lista[0] + lista[1]
    if lista[0] == lista[1]:
        print(f'{cores["ciano"]}Parece que empatamos! Vamos de novo.{cores["limpa"]}')
    elif 'pedratesoura' in juntos or 'tesourapedra' in juntos:
        if lista[0] == 'pedra':
            print(choice(msg_perda))
            computador += 1
        else:
            print(choice(msg_vitoria))
            jogador += 1
    elif 'tesourapapel' in juntos or 'papeltesoura' in juntos:
        if lista[0] == 'tesoura':
             print(choice(msg_perda))
             computador += 1
        else:
             print(choice(msg_vitoria))
             jogador += 1
    elif 'papelpedra' in juntos or 'pedrapapel' in juntos:
        if lista[0] == 'papel':
            print(choice(msg_perda))
            computador += 1
        else:
             print(choice(msg_vitoria))
             jogador += 1
 
def contagem(var1, var2):
    global nome
    if var1 > var2:
        print(f'O {cores["ciano"]}computador{cores["limpa"]} fez mais pontos.')
    elif var1 < var2:
        print(f'{cores["magenta"]}{nome}{cores["limpa"]} fez mais pontos.')
    else:
        print(f'O {cores["ciano"]}computador{cores["limpa"]} e o {cores["magenta"]}jogador{cores["limpa"]} fizeram a mesma quantidade de pontos.')
    
opcoes = ['pedra', 'papel', 'tesoura']
msg_vitoria = ['\33[32mParece que eu perdi. Parabéns! Um ponto para você.\33[m', '\33[32mVocê conseguiu me vencer! Parece que está com sorte. Parabéns!\33[m', '\33[32mInfelizmente eu perdi, mas vencerei na próxima! Parabéns!\33[m']
msg_perda = ['\33[31mHaha! Eu venci! Um ponto para mim.\33[m', '\33[31mParece que eu venci. Melhore na próxima!\33[m', '\33[31mVai precisar de muito mais esforço para me derrotar. Tenta na próxima!\33[m', '\33[31mVenci!!! Me de meus parabéns hahaha.\33[m']       
computador = jogador = 0    
                
# Programa principal    
titulo('Pedra | Papel | Tesoura')

# Nome do jogador
while True:
    nome = str(input('Digite seu nome: ')).strip().title()
    print(f'O nome digitado foi {cores["magenta"]}{nome}{cores["limpa"]}.')
    rest = ' '
    while rest not in 'SN':
        rest = str(input('Tem certeza do seu nome? [S/N] ')).strip().upper()[0]
    if rest == 'S':
        break
    linha()
linha()
   
# O jogo       
while True:
    # Pedra, papel ou tesoura
    lances = []
    lances.append(escolha_computador(opcoes))
    escolha_jogador = ' '
    while escolha_jogador not in 'pedrapapeltesoura':
        print(f'''Opções:
 - {cores["vermelho"]}[0] Pedra {cores["limpa"]}
 - {cores["verde"]}[1] Papel {cores["limpa"]}
 - {cores["azul"]}[2] Tesoura {cores["limpa"]}''')
        try:
            escolha_jogador = int(input(f'{cores["amarelo"]}Pedra, Papel ou Tesoura? {cores["limpa"]}'))
        except:        
            print('Essa opção não existe. Vamos lá, escolha!')
            continue
        if escolha_jogador == 0:
            escolha_jogador = opcoes[0]
        elif escolha_jogador == 1:
            escolha_jogador = opcoes[1]
        elif escolha_jogador == 2:
            escolha_jogador = opcoes[2]
        lances.append(escolha_jogador)
    
    # Quem venceu?
    print(f'Você escolheu {cores["cinza"]}{escolha_jogador}{cores["limpa"]}')
    mostrar(lances[0])
    
    jogo(lances)
    
    # Mensagem para jogar novamente
    linha()
    rest = ' '
    while rest not in 'SN':
        rest = str(input(f'{cores["amarelo"]}Quer jogar novamente? [S/N]{cores["limpa"]} ')).strip().upper()[0]
    if rest == 'N':
        linha()
        temporizador('Calculando a pontuação')
        break
    
# Cálculo da pontuação
print(f'\nPontuação do {cores["ciano"]}computador{cores["limpa"]}: {computador}')
print(f'Pontuação do {cores["magenta"]}jogador{cores["limpa"]}: {jogador}')
contagem(computador, jogador)
linha()
sleep(1.5)
print(f'Foi muito divertido jogar com você, {cores["magenta"]}{nome}{cores["limpa"]}! Volte sempre!')

