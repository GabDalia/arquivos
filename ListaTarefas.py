# Lista de tarefas
# Crie um programa que permita:
# Adicionar uma tarefa
# Ver todas as tarefas
# Remover uma tarefa
# Sair
# Salve tudo em tarefas.txt.

def adicionarTarefas():
    while True:
        try:
            qt = int(input('Quantas tarefas deseja adicionar? '))
            break
        except ValueError:
            print("Opção inválida!")
    for i in range (qt):
        tarefa = input('Nome da tarefa: ')
        with open ('listaTarefas.txt','a') as arquivo:
            arquivo.write(f'{tarefa}\n')

def verTarefas():
    with open('listaTarefas.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        if conteudo == '':
            print('A lista de tarefas está vazia!')
        else:
            print(conteudo)

def removerTarefas():
    while True:
        try:
            qt = int(input('Quantas tarefas deseja remover? '))
            break
        except ValueError:
            print("Opção inválida!")
    for i in range(qt):
        encontrou = False  # Para avisar que a remocao foi efetuada apenas se a tarefa existir
        remover = input('Qual o nome da tarefa que deseja remover? ')
        with open('listaTarefas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        with open('listaTarefas.txt','w') as arquivo:
            for linha in linhas:
                if linha.strip()  != remover:
                    arquivo.write(linha)
                else:
                    encontrou = True
            if encontrou == True:
                print(f"Tarefa '{remover}' removida com sucesso!")
            else:
                print(f"A tarefa '{remover}' não estava cadastrada!")




print('\n      ⊹₊˚‧︵‿₊୨MENU୧₊‿︵‧˚₊⊹\n')
print('❥︎ (1) - Adicionar novas tarefas')
print('❥︎ (2) - Ver tarefas pendentes')
print('❥︎ (3) - Remover tarefas')
print('❥︎ (4) - Sair')

opcao = 0

while True:
    opcao = input('')
    if opcao == '1':
        adicionarTarefas()
    elif opcao == '2':
        verTarefas()
    elif opcao == '3':
        removerTarefas()
    elif opcao == '4':
        break
    else:
        print('Opção inválida!!!')



