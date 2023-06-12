from cadastro_animais import *
from os import name, system
from time import sleep

dados_pessoas = open('dados_pessoas.txt', 'a', encoding='utf-8')


def info_pessoa():
    limpar()
    print('\n\tINFORME OS DADOS PESSOAIS')

    n = input('Nome: ')
    while not n.isalpha():
        print('Nome inválido!')
        n = input('Nome: ')

    s = input('Sobrenome: ')
    while not s.isalpha():
        print('Sobrenome inválido!')
        s = input('Sobrenome: ')

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

    print('Endereço')
    rua = input(str('Rua: '))
    lote = input(str('Lote: '))
    quadra = input(str('Quadra: '))
    casa = input(str('Casa: '))

    end_format = 'Rua:' + rua + ';' + 'Lote:' + lote + ';' + 'Quadra:' + quadra + ';' + 'Casa:' + casa

    tel = input('Telefone com DDD: ')
    while not tel.isnumeric():
        print('Telefone inválido!')
        tel = input('Telefone com DDD: ')
    while len(tel) < 11:
        print('telefone inválido!')
        tel = input('Telefone com DDD: ')
   
    dados_pessoas.write(f'{n} {s} {cpf} {i_p} {end_format} {tel}')
    dados_pessoas.close()

def quer_doar():
    limpar()
    dados_pessoas = open('dados_pessoas.txt', 'a', encoding='utf-8')
    cadastrar_animal()
    dados_pessoas.close()


def quer_adotar():
    limpar()
    dados_pessoas = open('dados_pessoas.txt', 'a', encoding='utf-8')

    especie = str(input('Qual espécie quer adotar? '))
    preferencia = str(input('Possui alguma preferência? '))

    with open('dados_pessoas.txt', 'a'):
        dados_pessoas.write(f' {especie} {preferencia}\n')
        dados_pessoas.close()

def doar_e_adotar():
    limpar()
    dados_pessoas = open('dados_pessoas.txt', 'a', encoding='utf-8')
    cadastrar_animal()
    dados_pessoas.close()
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
