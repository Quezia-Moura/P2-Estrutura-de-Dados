from os import name, system
from time import sleep

dados_canino = open('dados_canino.txt', 'a', encoding='utf-8')
dados_felinos = open('dados_felinos.txt', 'a', encoding='utf-8')
dados_aves = open('dados_aves.txt', 'a', encoding='utf-8')
dados_peixes = open('dados_peixes.txt', 'a', encoding='utf-8')
dados_outros = open('dados_outros.txt', 'a', encoding='utf-8')

dados_pessoas = open('dados_pessoas.txt', 'a', encoding='utf-8')


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

    dados_canino.write(f'Tipo: {t}, Idade: {i}, Cor: {c}, Porte: {p}, Particularidade: {part}')


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

    dados_felinos.write(f'Tipo: {t}, Idade: {i}, Cor: {c}, Porte: {p}, Particularidade: {part}')


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

    dados_aves.write(f'Tipo: {t}, Idade: {i}, Cor: {c}, Porte: {p}, Particularidade: {part}')


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

    dados_peixes.write(f'Tipo: {t}, Idade: {i}, Cor: {c}, Porte: {p}, Particularidade: {part}')


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

    dados_outros.write(f'Tipo: {t}, Idade: {i}, Cor: {c}, Porte: {p}, Particularidade: {part}')


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


def info_pessoa():
    limpar()
    print('\n\tINFORME OS DADOS PESSOAIS')

    n = input('Nome: ')
    while not n.isalpha():
        print('Nome inválido!')
        n = input('Nome: ')

    cpf = input('CPF: ')
    while not cpf.isnumeric():
        print('CPF inválido!\nDigite apenas números!')
        cpf = input('CPF: ')
    while len(cpf) < 11:
        print('CPF inválido!\nO CPF informado deve conter 11 digitos!')
        cpf = input('CPF: ')

    i_p = input('Idade: ')
    while not i_p.isnumeric():
        print('Idade inválida!')
        i_p = input('Idade: ')

    end = input(str('Endereço: '))

    tel = input('Telefone com DDD: ')
    while not tel.isnumeric():
        print('Telefone inválido!')
        tel = input('Telefone com DDD: ')
    while len(tel) < 11:
        print('telefone inválido!')
        tel = input('Telefone com DDD: ')
   
    dados_pessoas.write(f'\nNome: {n}, CPF: {cpf}, Idade: {i_p}, Endereço: {end}, Telefone: {tel}')


def quer_doar():
    limpar()
    cadastrar_animal()


def quer_adotar():
    limpar()
    especie = str(input('Qual espécie quer adotar? '))
    preferencia = str(input('Possui alguma preferência? '))

    with open('dados_pessoas.txt', 'a'):
        dados_pessoas.write(f' | Espécie que quer adotar: {especie}, Preferência: {preferencia}')


def doar_e_adotar():
    limpar()
    cadastrar_animal()
    quer_adotar()


def cadastrar_pessoa():
    limpar()
    info_pessoa()
    limpar()
    print('''
    ||===============================||
    ||                               ||
    ||    ( 1 ) QUER DOAR            ||
    ||    ( 2 ) QUER ADOTAR          ||
    ||    ( 3 ) DOAR E ADOTAR        || 
    ||                               ||
    ||===============================||
    ''')
    o = input('Selecione uma opção: ')
    if o == '1':
        quer_doar()
    if o == '2':
        quer_adotar()
    if o == '3':
        doar_e_adotar()



def limpar():
    if name == 'nt':
        limpar = 'cls'
    else:
        limpar = 'clear'
    system(limpar)
