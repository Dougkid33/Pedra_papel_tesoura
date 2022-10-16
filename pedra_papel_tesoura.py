"""
Meu primeiro projeto Python.
Jogo de Pedra, papel e tesoura, para inciantes da linguagem.
Objetivo é testar minha lógica e também conhecimento da sintaxe.

tENTAREMOS também acrescentar tela gráfica
"""
# criação das variáveis e importando a biblioteca random
import random

while True:
    escolhas = ["pedra", "papel", "tesoura"]

    maquina = random.choice(escolhas)
    jogador = None

    while jogador not in escolhas:
        jogador = input("pedra, papel ou tesoura ?").lower()

    if jogador == maquina:
        print(f'Computador: {maquina}')
        print(f' Jogador: {jogador}')
        print("EMPATE TÉCNICO !!!")

    elif jogador == "pedra":
        if maquina == "papel":
            print(f'Computador: {maquina}')
            print(f' Jogador: {jogador}')
            print("Você perdeu !!!")
        if maquina == "tesoura":
            print(f'Computador: {maquina}')
            print(f' Jogador: {jogador}')
            print("Você GANHOU !!!")

    elif jogador == "papel":
        if maquina == "tesoura":
            print(f'Computador: {maquina}')
            print(f' Jogador: {jogador}')
            print("Você perdeu !!!")
        if maquina == "pedra":
            print(f'Computador: {maquina}')
            print(f' Jogador: {jogador}')
            print("Você GANHOU !!!")

    elif jogador == "tesoura":
        if maquina == "pedra":
            print(f'Computador: {maquina}')
            print(f' Jogador: {jogador}')
            print("Você perdeu !!!")
        if maquina == "papel":
            print(f'Computador: {maquina}')
            print(f' Jogador: {jogador}')
            print("Você GANHOU !!!")
    jogar_novamente = input(" Jogar Novamente? (sim/não): ").lower()

    if jogar_novamente != "sim":
        break

print("GAME OVER!!")
