# 5. Carrinho de Compras

# Faça um programa que:

# Tenha um dicionário com produtos e preços.

# Outra estrutura (dicionário ou lista) para o carrinho.

# Use uma função para adicionar itens ao carrinho.

# Use um loop para que o usuário continue comprando.

# Use condições para verificar se o produto existe.

# Ao final, calcule e exiba o valor total da compra.


produtos = {
    "Arroz": 7.50,
    "Feijão": 6.20,
    "Açúcar": 3.90,
    "Macarrão": 4.50,
    "Óleo de soja": 5.80,
    "Café": 12.00,
    "Leite": 4.20,
    "Manteiga": 7.00,
    "Pão de forma": 6.50,
    "Sabonete": 2.00
}

carrinho = []

def adicionar_itens(codigo, produtos, carrinho):
    lista_produtos = list(produtos.keys())
    
    #Verificar se o código é válido
    if 1 <= codigo <= len(lista_produtos):
        produto = lista_produtos[codigo -1] # pegar pelo índice
        carrinho.append(produto)
        print(f" {produto} adicionado ao carrinho")
    else:
        print("código inválido")
#PROGRAMA PRINCIPAL
print("=-" *20)
print(f"{'COD':<3}  {'PRODUTO':<15}{'PREÇO':>7}")
print("=-" *20)

for i, p in enumerate(produtos):
    print(f' {i+1:<3} {p:<15} $ {produtos[p]:>5.2f}')
print("")

while True:
    codigo = int(input("Digite o código do produto que desejar adicionar ao carrinho: "))
    adicionar_itens(codigo, produtos, carrinho)
    resp = input("Quer continuar [S] para sim e [N] para não: ").upper()
    
    if resp == 'N':
        break

print("=-" *20)
print(f"{'COD':<3}  {'PRODUTO':<15}{'PREÇO':>7}")
print("=-" *20)
total = 0
for i ,item in enumerate(carrinho):
    print(i+1, end="  ")
    preco = produtos[item]
    total += preco
    print(f"  {item:<15} $ {preco:.2f}")
print("")
print(f"Total a pagar........${total:.2f} ")
print("=-" *20)