from os import name, system
from time import sleep

dados_canino = open('dados_canino.txt', 'r', encoding='utf-8')
dados_felinos = open('dados_felinos.txt', 'r', encoding='utf-8')
dados_aves = open('dados_aves.txt', 'r', encoding='utf-8')
dados_peixes = open('dados_peixes.txt', 'r', encoding='utf-8')
dados_outros = open('dados_outros.txt', 'r', encoding='utf-8')

dados_pessoas = open('dados_pessoas.txt', 'r', encoding='utf-8')

lista = []
lista_p = []

for linha_pessoa in dados_pessoas:
    index = linha_pessoa.split(' ')
    field1 = index[0]
    field2 = index[1]
    field3 = index[2]
    field4 = index[3]
    field5 = index[4]
    field6 = index[5]
    field7 = index[6]
    field8 = index[7]

    lista_p.append([field1, field2, field3, field4, field5, field6, field7, field8])


for l_c in dados_canino:
    indices = l_c.split(' ')
    c_c1 = indices[0]
    c_c2 = indices[1]
    c_c3 = indices[2]
    c_c4 = indices[3]
    c_c5 = indices[4]
    
    lista.append([c_c1, c_c2, c_c3, c_c4, c_c5])

for l_f in dados_felinos:
    indices = l_f.split(' ')
    c_f1 = indices[0]
    c_f2 = indices[1]
    c_f3 = indices[2]
    c_f4 = indices[3]
    c_f5 = indices[4]
    
    lista.append([c_f1, c_f2, c_f3, c_f4, c_f5])

for l_a in dados_aves:
    indices = l_a.split(' ')
    c_a1 = indices[0]
    c_a2 = indices[1]
    c_a3 = indices[2]
    c_a4 = indices[3]
    c_a5 = indices[4]
    
    lista.append([c_a1, c_a2, c_a3, c_a4, c_a5])

for l_p in dados_peixes:
    indices = l_p.split(' ')
    c_p1 = indices[0]
    c_p2 = indices[1]
    c_p3 = indices[2]
    c_p4 = indices[3]
    c_p5 = indices[4]
    
    lista.append([c_p1, c_p2, c_p3, c_p4, c_p5])

for l_o in dados_outros:
    indices = l_o.split(' ')
    c_o1 = indices[0]
    c_o2 = indices[1]
    c_o3 = indices[2]
    c_o4 = indices[3]
    c_o5 = indices[4]
    
    lista.append([c_o1, c_o2, c_o3, c_o4, c_o5]) 


# def relatório():
#     limpar()
        
#     for lis_int in lista_p:
#         for pessoa in lis_int:
#             esp = pessoa[6]

#     for lista_interna in lista:
#         for animal in lista_interna:
#             ani = animal[0]

#     if esp == ani:
#         print(f'{esp}\n{ani}')


def animais_disponíveis():
    limpar()
    animal_de_interesse = str(input('Animal de Interesse: '))
    caracteristicas = input('Característica desejada: ')

    for lista_interna in lista:
        for animal in lista_interna:
            if animal_de_interesse == animal and caracteristicas in lista_interna:
                print(f'\nAnimal: {animal}, Idade: {lista_interna[1]}, Cor: {lista_interna[2]}, Porte: {lista_interna[3]}, Particularidade: {lista_interna[4]}')


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
