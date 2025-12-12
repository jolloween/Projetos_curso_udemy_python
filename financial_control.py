# 2. Controle Financeiro

# Faça um sistema que:

# Armazene despesas em um dicionário no formato {categoria: valor}.

# Tenha função para adicionar despesas.

# Use loop para permitir várias inserções.

# Ao final, calcule e mostre:

# total gasto

# maior despesa

# categoria mais usada
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()
despesas = {}

def atualizar_gastos(categoria, valor, despesas):
    despesas[categoria] = valor



while True:
    print("=-" *20)
    categoria = input('Categoria: ')
    valor = float(input("Valor do gasto: "))

    atualizar_gastos(categoria, valor, despesas)
    
    while True:
        resp = input("quer continuar 's' para sim e 'n' para não? ").lower()
        if resp not in ('s', 'n'):
            print("'s' para sim e 'n' para não")
            continue
        else:
            break
        
    if resp == 'n':
        break

limpar_tela()
for c, v in despesas.items():
    print("=-" *20)
    print(f'categoria: {c} gasto: {v:.2f}')
print("=-" *20)

# key= diz ao Python como comparar os elementos.
#despesas.get retorna o valor da chave no dicionário.
maior_categoria = max(despesas, key=despesas.get)
maior_valor = despesas[maior_categoria]
print(f"Maior gasto foi em '{maior_categoria}' no valor de R$ {maior_valor:.2f}")

total = sum(despesas.values())
print(f'total de gastos foi: ${total:.2f}')