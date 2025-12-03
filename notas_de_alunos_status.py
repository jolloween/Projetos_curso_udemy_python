aluno = []

# 1º validação
#caso o usuário digite letras ou número negativos
#será solicitado a quantidade de alunos a serem cadastrados
while True:
    try:
        qtd = input("Digite a quantidade de alunos: ")
        if qtd.isdigit():
            quantidade = int(qtd)
            break
        else:
            print("⚠️  Por favor, digite a quantidade de alunos a serem cadastrados")
    except ValueError:
        print(".")

#2ª Validação
#Será solicitado nome(s) do(s) aluno(s)

i = 0
for i in range(0, quantidade):
    
    nome = input("Nome do aluno: ")
    while True:
        try:
            n1 = float(input('primeira nota: '))
            n2 = float(input("Segunda nota: "))
            if 0 <= n1 and 0 <= n2: #Não é permitido números negativos
                break
            else:
                print("⚠️  Digite notas entre 0 e 10")
            
        except ValueError: #não deixa digitar letras em notas
            print('Digite uma nota válida')
            
    
    notas = [n1, n2]
    media = sum(notas) / len(notas)
    if media >= 7:
        status = "aprovado"
    elif media >= 5:
        status = "recuperação"
    else:
        status = "reprovado"
    
    aluno.append([nome, notas, media, status])
    print(aluno)

    #Relatório final
aprovados = 0
recuperacao = 0
reprovados = 0

for i, (nome, notas, media, status) in enumerate(aluno):
    print(f"{i+1}. Nome: {nome}")
    print(f"   Notas: {notas}")
    print(f"   Média: {media:.2f}")
    print(f"   Status: {status}\n")



    if status == "aprovado":
        aprovados += 1
    elif status == "recuperação":
        recuperacao += 1
    else:
        reprovados += 1

print("===RESUMO===")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")