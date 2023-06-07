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
    ...
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
    endereço = input('Endereço: ')
    while not endereço.isalpha():
        print('Endereço inválido')
        endereço = input('Endereço: ')
    telefone = input('Telefone: ')
    while not telefone.isnumeric():
        print('Telefone inválido!')
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

