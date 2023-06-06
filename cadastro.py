canino = {'Tipo: ': 'Cão', 'Idade: ': '2', 'Cor: ': 'Bege', 'Porte: ': 'Médio', 'Particularidade: ': 'Não'}



def cadastrar_animal():
    ...
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
    p = input('Porte: ')
    part = input('Particularidade: ')


def info_pessoa():
    ...
    print('\n\tINFORME OS DADOS PESSOAIS')
    nome = input('Nome: ')
    cpf = input('CPF: ')
    idade = int(input('Idade: '))
    endereço = input('Endereço: ')
    telefone = input('Telefone: ')



def quer_doar():
    ...

def quer_adotar():
    ...

def doar_e_adotar():
    ...


def cadastrar_pessoa():
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
    ...

