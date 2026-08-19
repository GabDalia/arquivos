def adicionarProdutos(qtProdutos):
    for i in range (qtProdutos):
        produto = input('Digite o nome do produto: ')
        with open('lista.txt','a') as arquivo:
            arquivo.write(f'{produto}\n')
    print('Produtos adicionado com sucesso!')

def removerProdutos():
    remover = input('Digite o nome do produto que você deseja remover: ')
    with open('lista.txt','r') as arquivo:
        linhas = arquivo.readlines()
    with open('lista.txt','w') as arquivo:
        for linha in linhas:
            if linha.strip() != remover:
                arquivo.write(linha)
    print('Produto removido com sucesso!')

def leitura():
    with open('lista.txt','r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
#Menu
opcao = 0

print('\n======== MENU =========')
print('[1] Adicionar Produtos')
print('[2] Remover Produtos')
print('[3] Ver Lista')
print('[4] Sair')

while opcao != 4:
    opcao = int(input('\nDigite uma das opções:'))
    if opcao == 1:
        qt = int(input('Quantos produtos você deseja adicionar na lista? '))
        adicionarProdutos(qt)
    elif opcao == 2:
        removerProdutos()
    elif opcao == 3:
        leitura()
    else:
        print('Opção inválida!')
