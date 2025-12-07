# 1. Sistema de Cadastro de Alunos

# Crie um programa que:

# Use uma função para cadastrar um aluno (nome, idade e três notas).

# Armazene cada aluno em um dicionário.

# Use um loop para permitir cadastrar vários alunos.

# Use uma condição para parar quando o usuário digitar “não”.

# Ao final, exiba todos os alunos cadastrados.


import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastro_aluno():
    limpar_tela()
    aluno = {}
    
    aluno['nome'] = input('Nome do aluno: ')
    while True:
        try:
            aluno['idade'] = input("Ídade: ")
            if aluno['idade'].isdigit():
                break
                
            else:
                print('⚠️  Digite uma idade válida')
                continue
        except ValueError:
            print("")
        
    while True:
        try:
            nota1 = round(float(input('1º Nota: ')), 2)
            nota2 = round(float(input('2º Nota: ')), 2)
            nota3 = round(float(input('3º Nota: ')),2)
            aluno['notas'] = [nota1, nota2, nota3]
            break
        except ValueError:
            print("ERRO! Digite apenas números válidos.\n")
        
    return aluno

#Programa principal
alunos = []
while True:
    
    novo_aluno = cadastro_aluno()
    alunos.append(novo_aluno)

    while True:
        resp = input("Quer continuar [S] para sim e [N] para não: ").upper()
        if resp not in "SN":
            print("[S] para sim e [N] para não")
            continue
        break
    
    if resp == "N":
        break

limpar_tela()

print("=-" *20)
print("Alunos cadastratdos")
print("=-" *20)

for a in alunos:
    
    print(f'nome: {a['nome']}')
    print(f'idade: {a['idade']}')
    #exibe notas com 2 casas decimais
    nota_formatada = ', '.join(f'{n:.2f}' for n in a['notas'] ) #formata a nota com dois pontos flutuantes
    print(f'notas: {nota_formatada}')
    print("=-" *20)

