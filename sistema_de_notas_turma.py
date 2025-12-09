# 4. Sistema de Notas de Turma

# Construir um sistema que:

# Receba vários alunos e suas notas usando loop.

# Armazene cada aluno em um dicionário.

# Tenha uma função que calcule a média do aluno.

# Use condições para informar se ele está aprovado, recuperação ou reprovado.

# Mostrar ao final um boletim geral de todos os alunos.

cadastro = []


def media_notas(nota1, nota2):
    media = (nota1 + nota2) / len(aluno['notas'])
    return media

def situacao():

    if aluno['media'] >= 7:
        return 'aprovado'
    elif aluno['media' ] >= 5 and aluno['media' ] < 7:
        return 'recuperação'
    else:
        return 'Reprovado'
    
    
    #PROGRAMA PRINCIPAL
while True:
    aluno = {}
    aluno['nome']= input('Nome do aluno: ').title()

    n1 = float(input("Primiera nota: "))
    n2 = float(input("Segunda nota: "))

    aluno['notas'] = [n1, n2] # Adicona as notas no dicionário
    aluno['media'] = media_notas(n1, n2)
    aluno['situacao'] = situacao()
    cadastro.append(aluno)

    
    resp = input('quer continuar [S] para sim e [N] para não? ').upper().strip()

    if resp == 'N':
        break

for a in cadastro:
    print("=-" * 30)
    print(f"nome: {a['nome']}\nnotas: {a['notas'][0]:.2f} | {a['notas'][1]:.2f}\nmédia: {a['media']:.2f}\nsituação: {a['situacao']}")
