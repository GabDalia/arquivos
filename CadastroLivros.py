def cadastro():
    nome = input('Nome do livro: ')
    autor = input('Autor: ')
    ano = int(input('Ano: '))
    qt = int(input('Quantidade em estoque: '))
    with open("livros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.strip().split(';')
            if dados[0] == nome and dados[1] == autor and int(dados[2]) == ano:
                print("Esse livro já foi cadastrado anteriormente! ")
                return
    with open("livros.txt", "a") as arquivo:
        arquivo.write(f"{nome};{autor};{ano};{qt}\n")
        print("Livro cadastrado com sucesso!")

def listarLivros():
    with open("livros.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if not linhas:
            print("Não há livros cadastrados no sistema!")
        else:
            for linha in linhas:
                dados = linha.strip().split(';')
                print(f"Livro:{dados[0]}")
                print(f"Autor:{dados[1]}")
                print(f"Ano:{dados[2]}")
                print(f"Exemplares disponíveis:{dados[3]}")
                print("-"*25)
