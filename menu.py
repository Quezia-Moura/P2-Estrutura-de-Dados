from cadastro import *

while True:    
    print('''
    ||===============================||
    ||                               ||
    ||        ADOTE CONOSCO!         ||
    ||                               ||
    ||    ( 1 ) CADASTRAR ANIMAL     ||
    ||    ( 2 ) CADASTRAR PESSOA     ||
    ||    ( 3 ) CONSULTAR ANIMAL     || 
    ||    ( X ) SAIR                 ||
    ||                               ||
    ||===============================||
    ''')

    op = input('Selecione uma opção: ')
    if op == '1':
        cadastrar_animal()
    if op == '2':
        cadastrar_pessoa()
    if op == '3':
        consultar()
    if op == 'X' or op == 'x':
        break
