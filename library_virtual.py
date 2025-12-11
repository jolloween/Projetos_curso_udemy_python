# 7. Biblioteca Virtual

# Crie um sistema que:

# Use um dicionário para armazenar livros (título, autor, ano e status: disponível/emprestado).

# Tenha uma função para emprestar um livro.

# Use condições para verificar se o livro está disponível.

# Use um loop para permitir várias operações.

# Ao final, exiba todos os livros com seus status.



library = {
    "Drácula": {
        "autor": "Bram Stoker",
        "ano": 1897,
        "status": "disponível"
    },
    "Frankenstein": {
        "autor": "Mary Shelley",
        "ano": 1818,
        "status": "disponível"
    },
    "O Iluminado": {
        "autor": "Stephen King",
        "ano": 1977,
        "status": "disponível"
    },
    "It: A Coisa": {
        "autor": "Stephen King",
        "ano": 1986,
        "status": "disponível"
    },
    "O Exorcista": {
        "autor": "William Peter Blatty",
        "ano": 1971,
        "status": "disponível"
    },
    "A Assombração da Casa da Colina": {
        "autor": "Shirley Jackson",
        "ano": 1959,
        "status": "disponível"
    },
    "O Cemitério": {
        "autor": "Stephen King",
        "ano": 1983,
        "status": "disponível"
    },
    "Hell House – A Casa Infernal": {
        "autor": "Richard Matheson",
        "ano": 1971,
        "status": "disponível"
    },
    "Mexican Gothic": {
        "autor": "Silvia Moreno-Garcia",
        "ano": 2020,
        "status": "disponível"
    },
    "O Orfanato da Srta. Peregrine para Crianças Peculiares": {
        "autor": "Ransom Riggs",
        "ano": 2011,
        "status": "disponível"
    },
    "Carmilla": {
        "autor": "J. Sheridan Le Fanu",
        "ano": 1872,
        "status": "disponível"
    }
}

def lend_book(titulo, library):
    if titulo not in library:
        print("book not found")
        return
    # Check if it's already borrowed.
    if library[titulo] == 'emprestado':
        print(f'The {titulo} book is already borrowed.  ')
        return
    
    library[titulo]['status'] = 'emprestado'
    print(f'The book "{titulo}" has been successfully borrowed!')

while True:

    search_for_book = input("Which book would you like to rent? ")

    lend_book(search_for_book, library) # calls the Function
    
    while True:
        choice = input("Do you want to continue? [Y] for yes or [N] for no: ").upper()

        if choice in ('Y', 'N'):
            break
        else:
            print('Type "Y" for yes and "N" for no')
            
    if choice == 'N':
        break

print('=-' *20)
for k, v in library.items():
    print('=-' *20)
    print(f'titulo: {k}')
    print(f'autor: {v['autor']}')
    print(f'ano: {v['ano']}')
    print(f'status: {v['status']}')
print('=-' *20)

