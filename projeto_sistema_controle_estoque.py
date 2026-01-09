import os
import json
# ===== UTILIDADES =====
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# ============= ARQUIVOS =============
def carregar_dados(arquivo="produtos.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(produtos, arquivo="produtos.json"):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(produtos, f, ensure_ascii=False, indent=4)

#============ CADASTRO DE PRODUTOS ============
def cadastrar_produto(produtos):
    limpar_tela()

    # cadastra o ID do produto
    while True:
        limpar_tela()
        try:
            id_produto = int(input('Digite o ID do produto (0 para cancelar): '))
            
            # Verificar se o ID já existe
            id_existe = False
            for id in produtos:
                if id['id'] == id_produto:
                    id_existe = True
                    break
                    
            if id_existe:
                print("⚠️  ID já existe. Tente outro.")
                input("\nCarregue 'ENTER' para sair...")
                continue
            
            if id_produto == 0:
                return
            
            else:
                break

        except ValueError:
            print('⚠️  opção inválida. Digite um número.')
            input("\nCarregue 'ENTER' para continuar...")
            continue
    
    # cadastro do nome do produto
    while True:
        limpar_tela()
        nome_produto = input("Digite o nome do produto (0 para cancelar): ").strip()
        if nome_produto == '0':
            return
        
        elif nome_produto.isdigit():
            print("⚠️  Não pode conter números.")
            input("\nCarregue 'ENTER' para sair...")
            continue
        
        if not nome_produto.strip():
            print("⚠️  Não pode conter espaços.")
            input("\nCarregue 'ENTER' para sair...")
            continue
        
        
    # Verifica se já existe produto cadastrado
        produto_existe = False
        for produto in produtos:
            if produto['nome'] == nome_produto:
                produto_existe = True
                break
        
    #volta ao loop para cadastrar outro produto
        if produto_existe:
            print(f"⚠️  {nome_produto} já existe. Cadastre outro produto.")
            input("\nCarregue 'ENTER' para continuar...")
            continue
        else:
            break
    # ==== Loop para salva os valores dos produtos ====
    while True:

        try:
            valor_produto = float(input('Digite o valor do produto: $'))
            if valor_produto <= 0:
                print("⚠️  Digite um valor válido.")
                input("\nCarregue 'ENTER' para continuar...")
                continue
                
            else:
                break
        except ValueError:
            print("⚠️  Digite um valor válido.")
            input("\nCarregue 'ENTER' para continuar...")
            continue

    # ==== Loop para salvar a quantidade de produtos em estoque ====
    while True:
        try:
            qtd_produto = int(input("Digite a quantidade de produto em estoque: "))
            if qtd_produto < 0:
                print('⚠️ não pode ter números negativos.')
                input("\nCarregue 'ENTER' para continuar...")
                continue
            else:
                break
        except ValueError:
            print(f"Digite apenas números.")
            input("\nCarregue 'ENTER' para continuar...")
            continue

    #Salva os produtos em dicionário dentro de uma lista
    novo_produto = {'id': id_produto, 'nome': nome_produto, 'valor': valor_produto, 'quantidade': qtd_produto }
    produtos.append(novo_produto)
    #Salva os produtos no banco de dados
    salvar_dados(produtos)
    print(f"💾  {nome_produto} salvo com sucesso!")
    input("\nCarregue 'ENTER' para sair...")

# =========== LISTAR PRODUTOS =================
def listar_produtos(produtos):
    limpar_tela()

    print("=-=-"* 10)
    print(f"{'PRODUTOS CADASTRADOS':^40}")
    for lista in produtos:
        print("=-=-"* 10)
        print(f"ID: {lista['id']}")
        print(f"Produto: {lista['nome']}")
        print(f"Valor: ${lista['valor']:.2f}")
        print(f"Quantidade: {lista['quantidade']}")
    print("=-=-"* 10)
    input("\nCarregue 'ENTER' para sair...")
    
# =========== ENTRADA DE ESTOQUE ==============
def entrada_de_estoque(produtos):
    while True:
        try:
            #informa o id do produto
            id_produto = int(input('Digite o id do produto (0 para cancelar): '))
            if id_produto == 0:
                return
            
        except ValueError:
            print("⚠️  Apenas números é permtido!")
            input("\nCarregue 'ENTER' para continuar...")
            continue
        
        #Verifica se tem o produto no estoque
        produto_encontrado = None
        for produto in produtos:
            if produto['id'] == id_produto:
                produto_encontrado = produto
                break
    
        # se não há produto retorna ao loop
        if not produto_encontrado:
            print(f"ID: {id_produto} não encontrado, Tente outra vez.")
            input("\nCarregue 'ENTER' para continuar...")
            continue
        else:
            break

    # Adiciona produtos ao estoque escolhido
    while True:
        limpar_tela()
        print("==================== PRODUTO ENCONTRADO ======================")
        print(produto_encontrado)
        print('==============================================================')
        try:
            adicionar_estoque = int(input("Digite a quantidade de"
                    f" '{produto_encontrado['nome']}' que deseja adicionar:  "))
            if adicionar_estoque <= 0:
                print("⚠️  Não pode ser menor ou igual a zero.")
                input("\nCarregue 'ENTER' para continuar...")
                continue
            else:
                break
        except ValueError:
            print('⚠️  Apenas números inteiros é permitido.')
            input("\nCarregue 'ENTER' para continuar...")
            continue
        

    #adiciona produtos ao estoque
    produto_encontrado['quantidade'] += adicionar_estoque
    print('💾  Quantidade adicionada com sucesso')
    input("\nCarregue 'ENTER' para continuar...")

#=========== SAÍDA DE PRODUTOS ESTOQUE=========
def saida_de_estoque(produtos):
    while True:
        try:
            #informa o id do produto
            id_produto = int(input('Digite o id do produto (0 para cancelar): '))
            if id_produto == 0:
                return
            
        except ValueError:
            print("⚠️  Apenas números é permtido!")
            input("\nCarregue 'ENTER' para continuar...")
            continue
        
        #Verifica se tem o produto no estoque
        produto_encontrado = None
        for produto in produtos:
            if produto['id'] == id_produto:
                produto_encontrado = produto
                break
    
        # se não há produto retorna ao loop
        if not produto_encontrado:
            print(f"ID: {id_produto} não encontrado, Tente outra vez.")
            input("\nCarregue 'ENTER' para continuar...")
            continue
        else:
            break

    # saídas de produtos do estoque escolhido
    while True:
        limpar_tela()
        print("==================== PRODUTO ENCONTRADO ======================")
        print(produto_encontrado)
        print('==============================================================')
        try:
            saida_de_estoque = int(input("Digite a quantidade de"
                    f" '{produto_encontrado['nome']}' que deseja retirar:  "))
            
            # verifica quantidade de retirada se é maior que a do estoque
            if produto_encontrado['quantidade'] < saida_de_estoque:
                print("⚠️  Quantidade de estoque não pode ficar negativo.")
                input("\nCarregue 'ENTER' para continuar...")
                return
            else:
                break # retira a quantidade de produtos do estoque
        except ValueError:
            print('⚠️  Apenas números inteiros é permitido.')
            input("\nCarregue 'ENTER' para continuar...")
            continue
        

    #remove produtos do estoque
    produto_encontrado['quantidade'] -= saida_de_estoque
    print('💾  Quantidade retirada com sucesso')
    input("\nCarregue 'ENTER' para continuar...")

# =========== REMOVER PRODUTO =================
def remover_produtos(produtos):
    while True:
        try:
            id_produto = int(input('ID do produto (0 para cancelar):  '))
            if id_produto == 0:
                return
        except ValueError:
            print('⚠️  Apenas números é permitido.')
            input("\nCarregue 'ENTER' para continuar...")
            continue
        
        # procura produto por ID
        produto_encontrado = None
        for produto in produtos:
            if produto['id'] == id_produto:
                produto_encontrado = produto
                break
        
        if not produto_encontrado:
            print(f"'{id_produto}' não encontrado. Tente outra vez.")
            continue
        else:
            break
    
    # remover produto do estoque
    while True:
        limpar_tela()
        print("==================== PRODUTO ENCONTRADO ======================")
        print(produto_encontrado)
        print('==============================================================')
        
        resp = input(f"Tem certeza certeza que quer remover {produto_encontrado['nome']} [S/N]? " ).upper().strip()
        if resp == "N":
            print("Operação cancelada com sucesso.")
            input("\nCarregue 'ENTER' para sair...")
            return
        
        # remove o produto do estoque
        elif resp == "S":
            produtos.remove(produto_encontrado)
            print(f"💾 removido com sucesso")
            input("\nCarregue 'ENTER' para sair...")
            return
        else:
            print("⚠️  Opção inválida.")
            input("\nCarregue 'ENTER' para continuar...")
# =========== LISTA DE PRODUTOS ===============
produtos = carregar_dados()

# ============= MENU DO PROGRAMA ==============
def menu():
    print("=-=-" *6)
    print(f"{'MENU':^24}")
    print("=-=-" *6)
    print('[1] Cadastrar produto')
    print('[2] Listar produtos')
    print('[3] Entrada de estoque')
    print('[4] Saída de estoque')
    print('[5] Remover produto')
    print('[6] Sair')

# ============= PROGRAMA PRINCIPAL ============
while True:
    while True:
        limpar_tela()
        menu()
    # Validações das opções do menu
        try:
            op = int(input('\nEscolha a opção desejada: '))
            if op < 1 or op > 9:
                print('⚠️  opção inválida')
                input("\nCarregue 'ENTER' para sair...")
            else:
                break
        except ValueError:
            print("⚠️  Opção inválida")
            input("\nCarregue 'ENTER' para sair...")
        
    # Escolha da opção do menu
    match op:
        case 1:
            cadastrar_produto(produtos)
        case 2:
            listar_produtos(produtos)
        case 3:
            entrada_de_estoque(produtos)
        case 4:
            saida_de_estoque(produtos)
        case 5:
            remover_produtos(produtos)
        case 6:
            break

print("==== LISTA COM DICIONÁRIO DOS PRODUTOS ====\n")
print(produtos)
