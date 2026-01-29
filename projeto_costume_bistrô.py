import os
import json
import unicodedata
import pandas as pd

#======== UTILIDADES ========
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Ordena por ordem alfabética ignorando acentuações,
# maiusculas, minusculas e etc...
def normalizar(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

#====== ARQUIVOS ========
def carregar_dados(arquivo="vinhos.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(vinhos, arquivo="vinhos.json"):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(vinhos, f, ensure_ascii=False, indent=4)
        

#===== CADASTRo DE VINHOS ========
def cadastrar_vinho(vinhos):
    
    while True:
        limpar_tela()
        nome = input('Digite o nome do vinho (Digite 0 para sair): ').strip()
        
        if nome == '0':
            print('❌  Operação cancelada pelo usuário.')
            input('\nTecle enter para sair...')
            return
        if not nome.strip():
            print("⚠️  Não pode conter espaços em branco.")
            input('\nTecle enter para continuar...')
            continue
        for vinho in vinhos:
            if normalizar(vinho['nome']).lower() == normalizar(nome).lower():
                print('Vinho já cadastrado!')
                input('\nTecle enter para sair...')
                return
        tipo = input('Tipo do vinho: ').strip()

        while True:
            regiao = input('Região [Porto/Douro]: ').title().strip()
            if regiao in ('Porto', 'Douro'):
                break
            else:
                print('Digite apenas Porto ou Douro')
                continue

        while True:
            try:
                preco = float(input('Preço da garrafa: $'))
                if preco <= 0:
                    print('⚠️  preço não pode ser zerou ou negativo')
                else:
                    break
            except ValueError:
                print('Preço inválido')
                continue
        dados_vinho = {'nome': nome, 'tipo': tipo, 'regiao': regiao, 'quantidade': 0, 'preco': preco}
        
        
        vinhos.append(dados_vinho)
        vinhos.sort(key=lambda v: normalizar(v['nome']))
        print(f"💾  {nome} cadastrado com sucesso!")
        salvar_dados(vinhos)

        while True:
            resp = input('Quer continuar [S/N]?').strip().upper()
            if resp in ('S', 'N'):
                break
            print('⚠️  Digite S para sim e N para não.')
        if resp == 'N':
            return

#===== EXPORTAR PARA EXCEL ======
def exportar_para_excel(vinhos, arquivo="vinhos.xlsx"):
    if not vinhos:
        print("⚠️  Não há vinhos para exportar.")
        input('\nTecle enter para sair...')
        return
    
    df = pd.DataFrame(vinhos)
    df.to_excel(arquivo, index=False)
    print(f"✅  Dados exportados com sucesso para {arquivo}")
    input('\nTecle enter para sair...')
#===== ADICIONA VINHO AO ESTOQUE =====
def adicionar_vinho(vinhos):

    while True:
        limpar_tela()
        print("=-" * 40)
        print(f"{'COD':<4} {'NOME':>10}   {'TIPO':>33}  {'QTD':>8} {'PREÇO':>14}")
        print("=-" * 40)

        for i, v in enumerate(vinhos, start=1):
            print('=-=-'*20)
            nome = v['nome'][:36]
            Tipo = v['tipo'][:8]
            # if v['quantidade'] > 0:
            print(f"{i:<4} {nome:<36}"
                f"     {Tipo:<12} {v['quantidade']:<10} {v['preco']:.2f}€")
        print('=-=-'*20)

        
        try:
            opc = int(input('Digite o índice do produto: '))
            if opc < 1 or opc > len(vinhos):
                print('⚠️  Opção inválida')
                input('\nCarregue Enter para continuar...')
                return
            # else:
            #     break
        except ValueError:
            print('⚠️  Opção inválida')
            input('\nCarregue Enter para continuar...')
            return
        
        produto_escolhido = vinhos[opc - 1]['nome']
        print(f"produto escolhido: {produto_escolhido}")

        for vinho in vinhos:
            if vinho['nome'] == produto_escolhido:
                while True:
                    try:
                        qtd = int(input('Quantidade que deseja adicionar: '))
                        if qtd < 0:
                            print('⚠️ Não pode ter números negativos.')
                            input('\nCarregue Enter para continuar...')
                            continue
                        else:
                            vinho['quantidade'] += qtd
                            print("💾 Adicinonado com sucesso. ")
                            # input('\nCarregue Enter para continuar...')
                            #Adiciona ao estoque e salva em lista json
                            vinhos.sort(key=lambda v: normalizar(v['nome']))
                            salvar_dados(vinhos)
                            break
                    except ValueError:
                        print('⚠️  Valor inválido.')
                        input('\nCarregue Enter para continuar...')
                        continue
        
        while True:
            resp = input('Quer continuar [S/N]?').strip().upper()
            if resp in ('S', 'N'):
                break
            print('⚠️  Digite S para sim e N para não.')
        if resp == 'N':
            return



#Retirada de vinho do estoque
def retirar_vinho(vinhos):
    
    while True:
        limpar_tela()

        for i, vinho in enumerate(vinhos, start=1):
            print('=-=-' * 25)
            print(f"{i}. Nome: {vinho['nome']}  Tipo: {vinho['tipo']}"
                f"  Região: {vinho['regiao']} Qtd: {vinho['quantidade']}")
        print('=-=-' * 25)

        try:
            opc = int(input('Digite o índice do produto: '))
            if opc < 1 or opc > len(vinhos):
                print('⚠️  Opção inválida')
                input('\nCarregue Enter para continuar...')
                return
            # else:
            #     break
        except ValueError:
            print('⚠️  Opção inválida')
            input('\nCarregue Enter para continuar...')
            return
        
        while True:
            try:
                qtd = int(input('Digite a quantidade de retirada desejada: '))
                if qtd < 0:
                    print('⚠️ Digite apenas numeros inteiros.')
                    continue
                if qtd > vinhos[opc - 1]['quantidade']:
                    print('Não há vinhos vinhos disponíveis para retirada.')
                else:
                    vinhos[opc - 1]['quantidade'] -= qtd
                    print('✅  Retirada feita com sucesso!')
                    input('Carregue enter para sair...')
                    return
            except ValueError:
                print('⚠️ Digite apenas numeros inteiros.')

#===== REMOVE O VINHO DA LISTA ========
def remover_vinho(vinhos):

    while True:
        limpar_tela()
        for i, vinho in enumerate(vinhos, start=1):
            print('=-=-' * 25)
            print(f"{i}. Nome: {vinho['nome']}  Tipo: {vinho['tipo']}"
                f"  Região: {vinho['regiao']} Qtd: {vinho['quantidade']}")
        print('=-=-' * 25)

        try:
            opc = int(input('Digite o índice do produto: '))
            if opc < 1 or opc > len(vinhos):
                print('⚠️  Opção inválida')
                input('\nCarregue Enter para continuar...')
                return
            else:
                break
        except ValueError:
            print('⚠️  Opção inválida')
            input('\nCarregue Enter para continuar...')
            return
        
    produto_escolhido = vinhos[opc - 1]
    vinhos.remove(produto_escolhido)
    print(f"🗑️  {produto_escolhido['nome']} removido com sucesso.")

    input('\nCarregue Enter para continuar...')

#===== EDITAR VINHO ======
def editar_vinho(vinhos):
    while True:
        limpar_tela()
        for i, vinho in enumerate(vinhos, start=1):
            print('=-=-' * 25)
            print(f"{i}. Nome: {vinho['nome']}  Tipo: {vinho['tipo']}"
                f"  Região: {vinho['regiao']} Qtd: {vinho['quantidade']}")
        print('=-=-' * 25)

        try:
            opc = int(input('Digite o índice do produto: '))
            if opc < 1 or opc > len(vinhos):
                print('⚠️  Opção inválida')
                input('\nCarregue Enter para continuar...')
                return
            else:
                break
        except ValueError:
            print('⚠️  Opção inválida')
            input('\nCarregue Enter para continuar...')
            return
        
    print('[1] para editar nome')
    print('[2] para editar tipo')
    print('[3] para editar região')
    print('[4] para editar preço')
    print('[5] para sair')

    escolha = int(input('digite sua opção:'))
    match escolha:

        case 1:
            nome = input('Nome do vinho (Enter p/cancelar): ').strip()
            if not nome.strip():
                input('Cancelado com sucesso. Enter para sair...')
                return
            vinhos[opc -1].update({'nome': nome})
            print(f'💾  editado "{nome}" com sucesso.')
            vinhos.sort(key=lambda v: normalizar(v['nome']))
            #salvar_dados(vinhos)
            input('\nCarregue Enter para continuar...')
        
        case 2:
            tipo = input('digite o tipo de vinho: ').strip()
            vinhos[opc -1].update({'tipo': tipo})
            print(f'💾  editado o tipo para "{tipo}" com sucesso.')
            vinhos.sort(key=lambda v: normalizar(v['nome']))
            #salvar_dados(vinhos)
            input('\nCarregue Enter para continuar...')

        case 3:
            regiao = input('Região: ')
            vinhos[opc - 1].update({'região': regiao})
            print(f'💾  editado o tipo para "{regiao}" com sucesso.')
            vinhos.sort(key=lambda v: normalizar(v['nome']))
            #salvar_dados(vinhos)
            input('\nCarregue Enter para continuar...')

        case 4:
            preco = float(input('Preço: $'))
            vinhos[opc - 1].update({'preco': preco})
            print(f'💾  editado o tipo para ${preco:.2f} com sucesso.')
            vinhos.sort(key=lambda v: normalizar(v['nome']))
            #salvar_dados(vinhos)
            input('\nCarregue Enter para continuar...')
        case 5:
            return
        
    

    input('\nCarregue Enter para continuar...')
#===== LISTA A QUANTIDADE DE VINHOS ======
def listar_vinhos(vinhos):
    print("=-" * 40)
    print(f"{'COD':<4} {'NOME':>10}  {'TIPO':>28}{'QTD':>8} {'PREÇO':>14}")
    print("=-" * 40)

    for i, v in enumerate(vinhos, start=1):
        nome = v['nome'][:30]
        if v['quantidade'] > 0:
            print(f"{i:<4} {v['nome']:<30}"
                f"     {v['tipo']:<10} {v['quantidade']:<11} {v['preco']:.2f}€")


    print("=-" * 40)
    input('\nTecle enter para sair...')

    
#===== MENU DO PROGRAMA =========
def menu():
    print('=-=-' * 7)
    print('MENU DE ESTOQUE DE VINHO')
    print('=-=-' * 7)
    print('[1] Cadastrar Vinho')
    print('[2] Adicionar vinho')
    print('[3] Retirar vinho')
    print('[4] Remover vinho')
    print('[5] Editar vinho')
    print('[6] Listar Estoque vinhos')
    print('[7] Exportar estoque para excel')
    print('[8] Sair')
    print('=-=-' * 7)

#==== LISTA DE DICIONÁRIOS =======
vinhos = carregar_dados()
# Ordena a lista por ordem alfabética antes de salvar
vinhos.sort(key=lambda v: normalizar(v['nome']))
salvar_dados(vinhos)

# ====== PROGRAMA PRINCIPAL =======
while True:
    
    while True:
        limpar_tela()
        menu()
        try:
            opcao = int(input('Escolha sua opção: '))
            if 1 > opcao > 6:
                print('⚠️  Opção inválida.')
            else:
                break
        except ValueError:
            print('⚠️  Opção inválida.')

    match opcao:
        case 1:
            cadastrar_vinho(vinhos)
        case 2:
            adicionar_vinho(vinhos)
        case 3:
            retirar_vinho(vinhos)
        case 4:
            remover_vinho(vinhos)
        case 5:
            editar_vinho(vinhos)
        case 6:
            listar_vinhos(vinhos)
        case 7:
            exportar_para_excel(vinhos)
        case 8:
            break

# print(vinhos)
