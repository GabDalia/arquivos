# 1. Lista de tarefas
# Crie um programa que permita:
# Adicionar uma tarefa
# Ver todas as tarefas
# Remover uma tarefa
# Sair
# Salve tudo em tarefas.txt.

def adicionarTarefas():
    qt = int(input('Quantas tarefas deseja adicionar? '))
    for i in range (qt):
        tarefa = input('Nome da tarefa: ')
        with open ('listaTarefas.txt','a') as arquivo:
            arquivo.write(f'{tarefa}\n')

def verTarefas():
    with open('listaTarefas.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

def removerTarefas():
    qt = int(input('Quantas tarefas deseja remover? '))
    for i in range(qt):
        remover = input('Qual o nome da tarefa que deseja remover? ')
        with open('listaTarefas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        with open('listaTarefas.txt','w') as arquivo:
            for linha in linhas:
                if linha.strip()  != remover:
                    arquivo.write(linha)




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

