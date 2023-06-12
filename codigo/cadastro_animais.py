from os import name, system
from time import sleep

dados_canino = open('dados_canino.txt', 'a', encoding='utf-8')
dados_felinos = open('dados_felinos.txt', 'a', encoding='utf-8')
dados_aves = open('dados_aves.txt', 'a', encoding='utf-8')
dados_peixes = open('dados_peixes.txt', 'a', encoding='utf-8')
dados_outros = open('dados_outros.txt', 'a', encoding='utf-8')


def canino():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')

    dados_canino.write(f'{t} {i} {c} {p} {part}\n')
    dados_canino.close()

def felinos():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')

    dados_felinos.write(f'{t} {i} {c} {p} {part}\n')
    dados_felinos.close()

def aves():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')

    dados_aves.write(f'{t} {i} {c} {p} {part}\n')
    dados_aves.close()

def peixes():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')

    dados_peixes.write(f'{t} {i} {c} {p} {part}\n')
    dados_peixes.close()

def outros():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')

    dados_outros.write(f'{t} {i} {c} {p} {part}\n')
    dados_outros.close()


def cadastrar_animal():
    limpar()
    print('''
    ||===============================||
    ||                               ||
    ||      ESCOLHA A ESPÉCIE        ||
    ||                               ||
    ||    ( 1 ) CANINO               ||
    ||    ( 2 ) FELINOS              ||
    ||    ( 3 ) AVES                 || 
    ||    ( 4 ) PEIXES               ||
    ||    ( 5 ) OUTRO                ||
    ||                               ||
    ||===============================||
    ''')

    op_e = input('Selecione uma opção: ')

    if op_e == '1':
        limpar()
        canino()
    if op_e == '2':
        limpar()
        felinos()
    if op_e == '3':
        limpar()
        aves()
    if op_e == '4':
        limpar()
        peixes()
    if op_e == '5':
        limpar()
        outros()    


def limpar():
    if name == 'nt':
        limpar = 'cls'
    else:
        limpar = 'clear'
    system(limpar)
