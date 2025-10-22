from random import randint
from time import sleep
from turtle import clear
import os

def clear():
    os.system('cls')
    print("\n" *10)

jogadas = ['Pedra', 'Papel', 'Tesoura']
computador_jogada = randint(0,2)
resultado = '\033[33mEMPATE!\033[m'

clear()

while True:
    print('-=' * 16)
    print('\033[34mJOGO DO PEDRA, PAPEL E TESOURA!\033[m')
    print('-=' * 16)

    print('''

    |======OPÇÕES======|
    | [ 0 ] PEDRA      |
    | [ 1 ] PAPEL      |
    | [ 2 ] TESOURA    | 
    |==================| 
                            \n''')

    jogador_jogada = int(input('\033[1;96mQual é a sua jogada?\033[m '))

    while jogador_jogada > 2:
        print('-=' * 22)
        print(f'\033[31mJogada: \033[m"{jogador_jogada}",\033[31m INVÁLIDA!\033[m \033[33mTente novamente...\033[m')
        print('-=' * 22)
        jogador_jogada = int(input('\033[1;96mVamos tentar mais uma vez! Qual é a sua jogada?\033[m '))
            
    if jogador_jogada < 3:
        if jogador_jogada == 0 and computador_jogada == 2 or jogador_jogada == 1 and computador_jogada == 0 or jogador_jogada == 2 and computador_jogada == 1:
            resultado = '\033[32mJOGADOR VENCE!\033[m\033[1;90m(Você)\033[m'
        elif jogador_jogada == computador_jogada:
            resultado =  '\033[33mEMPATE!\033[m [\033[1;90mNenhum dos Jogadores Venceram\033[m]'
        else:
            resultado = '\033[31mCOMPUTADOR VENCE!\033[m'

        sleep(0.5)
        print('\n\033[33mJO\033[m')
        sleep(0.6)
        print('\033[1;35mKEN\033[m')
        sleep(1)
        print(f'''\033[1;91mPO!!\033[m
        
    {'-=' * 14}
    Computador jogou: {jogadas[computador_jogada]}
    Jogador jogou: {jogadas[jogador_jogada]}
    {'-=' * 14}
    {resultado}''')


    reset = input("Tecle 0 para reset ou 1 para encerrar: ")
    if reset == "0":
        clear()
        continue
    else:
        clear()
        print("Encerrando o jogo...")
        sleep(2.5)
        clear()
        break