from os import name, system
from time import sleep

dados_canino = open('dados_canino.txt', 'r', encoding='utf-8')
dados_felinos = open('dados_felinos.txt', 'r', encoding='utf-8')
dados_aves = open('dados_aves.txt', 'r', encoding='utf-8')
dados_peixes = open('dados_peixes.txt', 'r', encoding='utf-8')
dados_outros = open('dados_outros.txt', 'r', encoding='utf-8')

dados_pessoas = open('dados_pessoas.txt', 'r', encoding='utf-8')

lista = []

def relatório():
    limpar()
    ...


def animais_disponíveis():
    limpar()
    animal_de_interesse = str(input('Animal de Interesse: '))
    # caracteristicas = input('Características desejadas: ')

    for linha in dados_canino:
        if animal_de_interesse in lista:
            print(linha)

    # for linha in zip(conteudo_c, conteudo_f, conteudo_a, conteudo_p, conteudo_o):
    #     if animal_de_interesse in linha and caracteristicas in linha:
    #         print(linha)


def consultar():
    limpar()
    print('''
    ||===============================||
    ||                               ||
    ||    ( 1 ) RELATÓRIO            ||
    ||    ( 2 ) ANIMAIS DISPONÍVEIS  ||
    ||                               ||
    ||===============================||
    ''')

    op_con = input('Selecione uma opção: ')
    if op_con == '1':
        relatório()
    if op_con == '2':
        animais_disponíveis()


def limpar():
    if name == 'nt':
        limpar = 'cls'
    else:
        limpar = 'clear'
    system(limpar)
