from dados import *
from os import name, system
from time import sleep


def canino():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')
    can['Tipo'].append(t)

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')
    can['Idade'].append(i)

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')
    can['Cor'].append(c)

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')
    can['Porte'].append(p)

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')
    can['Particularidade'].append(part)


def felinos():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')
    fel['Tipo'].append(t)

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')
    fel['Idade'].append(i)

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')
    fel['Cor'].append(c)

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')
    fel['Porte'].append(p)

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')
    fel['Particularidade'].append(part)

def aves():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')
    ave['Tipo'].append(t)

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')
    ave['Idade'].append(i)

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')
    ave['Cor'].append(c)

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')
    ave['Porte'].append(p)

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')
    ave['Particularidade'].append(part)

def peixes():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')
    pei['Tipo'].append(t)

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')
    pei['Idade'].append(i)

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')
    pei['Cor'].append(c)

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')
    pei['Porte'].append(p)

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')
    pei['Particularidade'].append(part)

def outros():
    print('\n\tINFORME DETALHES SOBRE O ANIMAL')

    t = input('Tipo: ')
    while not t.isalpha():
        print('Tipo inválido!')
        t = input('Tipo: ')
    out['Tipo'].append(t)

    i = input('Idade: ')
    while not i.isnumeric():
        print('Idade inválida!')
        i = input('Idade: ')
    out['Idade'].append(i)

    c = input('Cor: ')
    while not c.isalpha():
        print('Cor inválida!')
        c = input('Cor: ')
    out['Cor'].append(c)

    p = input('Porte: ')
    while not p.isalpha():
        print('Porte inválido!')
        p = input('Porte: ')
    out['Porte'].append(p)

    part = input('Particularidade: ')
    while not part.isalpha():
        print('Particularidade inválida!')
        part = input('Particularidade: ')
    out['Particularidade'].append(part)


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

    cpf = input('CPF sem traços e pontos: ')
    while not cpf.isnumeric():
        print('Cpf inválido!')
        cpf = input('CPF sem traços e pontos: ')
    while len(cpf) < 11:
        print('cpf inválido!')
        cpf = input('CPF sem traços e pontos: ')
    if len(cpf) == 11:
        cpf_formatado = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    print(cpf_formatado)

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
    if len(tel) == 11:
        print(tel)


def quer_doar():
    limpar()


def quer_adotar():
    limpar()
    especie = str(input('Qual espécie quer adotar? '))
    preferencia = str(input('Possui alguma preferência? '))
    

def doar_e_adotar():
    limpar()


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


      
def consultar():
    limpar()


def limpar():
    if name == 'nt':
        limpar = 'cls'
    else:
        limpar = 'clear'
    system(limpar)
