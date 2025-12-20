# 1. Cadastro de Clientes

# Cadastre clientes com: nome, idade e sexo.

# Use dicionário {nome: {idade, sexo}}

# Função para cadastrar.

# Função para listar todos.
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

clientes = {}

def cadastrar_cliente(clientes, nome, sexo, idade):
    if sexo == 'M':
        sexo = 'masculino'
    else:
        if sexo == 'F':
            sexo = 'feminino'

    dados = {'sexo': sexo, 'idade': idade}
    clientes[nome] = dados
    return

def lista_clientes(clientes):
    
    for nome_cliente, dados in clientes.items():
        print('=-' * 20)
        print(f"nome: {nome_cliente}  ")
        print(f"sexo: {dados['sexo']}")
        print(f"idade: {dados['idade']}")
    print('=-' * 20)
    return

limpar_tela()
while True:
    while True:
        nome = input('nome: ')
        if nome.isdigit():
            print('digite um nome válido')
        else:
            break
    while True:
        sexo = input('Digite o sexo: [M] para masculino e [F] para feminino:  ').upper()
        if sexo not in ('M', 'F'):
            print('⚠️  Por favor, digite "M" para masculino e "F" para feminino.')
        else:
            break

    while True:
        try:
            idade = int(input('idade: '))
            break
        except ValueError:
                print("⚠️  Por favor, digite uma idade válida")
        

    cadastrar_cliente(clientes, nome, sexo, idade)
    while True:
        resp = input('Quer continuar? [S/N] ').upper()
        if resp not in ("S", "N"):
            print('⚠️ Digite uma resposta válida.')
        else:
            break
    if resp == 'N':
        break

limpar_tela()
lista_clientes(clientes)

# print(clientes)