# 7. Controle de Estoque Avançado

# Produto {nome: {"quantidade": x, "preco": y}}

# Função para venda.

# Calcular faturamento.

import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


faturamento = 0
def venda_produto(produto, lista_produtos):
    global faturamento

    nome, detalhes = lista_produtos[produto - 1]
    
    quantidade = int(input(f"Quantidade de {nome} que queres comprar? "))
    
    if quantidade > detalhes['quantidade']:
        print(f"Quantidade insuficiente de {nome}")
    
    else:
        detalhes['quantidade'] -= quantidade
        total = detalhes['preco'] * quantidade
        faturamento += total
        print(f"Quantidade de {nome}: {detalhes['quantidade']} ")
        print(f"faturamento: ${faturamento:.2f}")
        

#PROGRAMA PRINCIPAL
limpar_tela()

produtos = {
    "Arroz": {"quantidade": 50, "preco": 5.99},
    "Feijão": {"quantidade": 30, "preco": 6.49},
    "Macarrão": {"quantidade": 40, "preco": 4.25},
    "Óleo": {"quantidade": 25, "preco": 7.50},
    "Açúcar": {"quantidade": 60, "preco": 3.99},
    "Sal": {"quantidade": 70, "preco": 2.50},
    "Café": {"quantidade": 35, "preco": 8.90},
    "Leite": {"quantidade": 45, "preco": 4.99},
    "Pão": {"quantidade": 50, "preco": 3.50},
    "Manteiga": {"quantidade": 20, "preco": 6.75}
}

lista_produtos = list(produtos.items())


print("---"*13)
print(f"{'COD':^3} | {'PRODUTO':^9} | {'QUANTIDADE':^11} | {'PREÇO':^7}")
print("---"*13)
for i, (nome, detalhes) in enumerate(lista_produtos, start=1):
    print(f"{i:^3} | {nome:^9} | {detalhes["quantidade"]:^11} |  ${detalhes["preco"]:^7.2F}")

while True:

    produto = int(input("Digite o código do produto ('0' para sair): "))
    if produto == 0:
        break
    venda_produto(produto, lista_produtos)

print(f"\nFaturamento total: $ {faturamento:.2f}")


# total_arroz = produtos["Arroz"]["quantidade"] * produtos["Arroz"]["preco"]
# print(total_arroz)