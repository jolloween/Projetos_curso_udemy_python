# ✅ Exercício 7 — Verificar presença de um item

# Crie uma função que receba uma lista de palavras e uma palavra para buscar.
# Retorne True se estiver na lista, ou False se não estiver.

# Exemplo:

# Entrada:
# Lista: ["maçã", "banana", "uva"]
# Busca: "uva"
# Saída: True

Lista = ["maçã", "banana", "uva"]

def verificar_item():
    for item in Lista:
        produto = input("Qual item deseja: ")

        if produto in item:
            return True
        else:
            return False
        
prdt = verificar_item()
print(prdt)