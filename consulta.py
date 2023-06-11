from dados import *
from time import sleep
from cadastro import limpar


def relatório():
    ...


def animais_disponíveis():
    # nomeeee = can['Tipo']
    # print(nomeeee)
    a_d = input('Animal de preferência: ')
    for a_d in can['Tipo']:
        print('Animal: ', a_d)
        indice = can['Tipo'].index(a_d)
        print('Idade: ', can['Idade'][indice])
        
        # print('Animal: {} \nÍndice: {}'.format(a_d, can['Tipo'].index(a_d)))


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


