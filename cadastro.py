from os import name, system
from time import sleep


canino = {'Tipo: ': 'Cão', 'Idade: ': '2', 'Cor: ': 'Bege', 'Porte: ': 'Médio', 'Particularidade: ': 'Não'}

def cadastrar_animal():
    limpar()
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



def info_pessoa():
    limpar() 
    print('\n\tINFORME OS DADOS PESSOAIS')

    nome = input('Nome: ')
    while not nome.isalpha():
        print('Nome inválido!')
        nome = input('Nome: ')

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

    idade = input('Idade: ')
    while not idade.isnumeric():
        print('Idade inválida!')
        idade = input('Idade: ')

    endereço = input(str('Endereço: '))

    telefone = input('Telefone com DDD: ')
    while not telefone.isnumeric():
        print('Telefone inválido!')
        telefone = input('Telefone com DDD: ')
    while len(telefone) < 11:
        print('telefone inválido!')
        telefone = input('Telefone com DDD: ')
    if len(telefone) == 11:
        print(telefone)

def quer_doar():
    limpar() 

def quer_adotar():
    limpar() 

def doar_e_adotar():
    limpar() 


def cadastrar_pessoa():
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
        info_pessoa()
        quer_doar()
    if o == '2':
        info_pessoa()
        quer_adotar()
    if o == '3':
        info_pessoa()
        doar_e_adotar()
        
        
      
def consultar():
    limpar() 


def limpar():
    if name == 'nt':
        limpar = 'cls'
    else:
        limpar = 'clear'
    system(limpar)
