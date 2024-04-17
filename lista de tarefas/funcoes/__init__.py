def add(dicionario, prioridade=30):
    print('-' * 42)
    quant = int(input("Quantas tarefas deseja adicionar? "))
    for c in range(0, quant):
        tarefa = input(f'{c+1}° Tarefa: ')
        # {'tarefa': ['111', '222'], 'situacao': [False, False], 'prioridade': [30, 30]}
        dicionario['tarefa'].append(tarefa)
        dicionario['situacao'].append(False)
        dicionario['prioridade'].append(prioridade)

    print(f'\033[0;32;40mTarefas adicionadas!\033[m')

def visualizar(dicionario):
    print('-' * 42)
    for c in range(0, len(dicionario['tarefa'])):
        print(f"\033[0;{dicionario['prioridade'][c]};40m[{'x' if dicionario['situacao'][c] == True else ' '}] {c} - {dicionario['tarefa'][c]}\033[m")

def concluir(dicionario):
    print('-' * 42)
    visualizar(dicionario)

    quant = int(input('Quantas tarefas deseja marcar como concluídas? '))

    for c in range(0, quant):
        tarefa = int(input(f'{c+1}° Tarefa: '))
        dicionario['situacao'][c] = True

def excluir(dicionario):
    print('-' * 42)
    visualizar(dicionario)
    indice = int(input("Tarefa a ser excluída: "))
    del(dicionario['tarefa'][indice])
    del(dicionario['situacao'][indice])
    del(dicionario['prioridade'][indice])

def priorizar(dicionario):
    print('-' * 42)
    visualizar(dicionario)
    tarefa = int(input('Tarefa: '))
    nivel = int(input('Nível de prioridade: '))

    if nivel == 1:
        dicionario['prioridade'][tarefa] = 32
    elif nivel == 2:
        dicionario['prioridade'][tarefa] = 33
    elif nivel == 3:
        dicionario['prioridade'][tarefa] = 31

def editar(dicionario):
    print('-' * 42)
    visualizar(dicionario)
    tarefa = int(input('Tarefa a ser editada: '))
    nova = input("Nova tarefa: ")
    dicionario['tarefa'][tarefa] = nova

def funcoes():
    print('-' * 42)
    print(' 1 - Visualizar lista \n',
         '2 - Adicionar tarefa \n',
         '3 - Marcar tarefa como concluída\n',
         '4 - Excluir tarefa\n',
         '5 - Priorizar\n',
         '6 - Editar\n',
         '7 - Sair')
    
    opc = int(input("Opção: "))

    return opc
