
def cadastro():
    nome = input('Nome do livro: ')
    autor = input('Autor: ')
    ano = int(input('Ano: '))
    qt = int(input('Quantidade em estoque: '))
    with open ("livros.txt", "a") as arquivo:
        arquivo.write(f"{nome};{autor};{ano};{qt}")

cadastro()
