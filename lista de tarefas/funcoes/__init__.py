def add(lista, prioridade=30):
    quant = int(input("Quantas tarefas deseja adicionar? "))

    for c in range(0, quant):
        tarefa = input(f'{c+1}° Tarefa: ')
        lista.append([tarefa, False, prioridade])

    print(f'\033[0;32;40mTarefas adicionadas!\033[m')

def visualizar(lista):
    for c in range(0, len(lista)):
        print(f"\033[0;{lista[c][2]};40m[{'x' if lista[c][1] == True else ' '}] {c} - {lista[c][0]}]\033[m")

def concluir(lista):
    visualizar(lista)

    quant = int(input('Quantas tarefas deseja marcar como concluídas? '))

    for c in range(0, quant):
        tarefa = int(input(f'{c+1}° Tarefa: '))
        lista[tarefa][1] = True

    print(f'\033[0;32;40mTarefas concluídas!\033[m')

def excluir(lista, indice):
    visualizar()
    lista.remove(lista[indice])

def priorizar(lista):
    visualizar()
    tarefa = int(input('Tarefa: '))
    nivel = int(input('Nível de prioridade: '))

    if nivel == 1:
        lista[tarefa][2] = 32
    elif nivel == 2:
        lista[tarefa][2] = 33
    elif nivel == 3:
        lista[tarefa][2] = 31

def funcoes():
    print(' 1 - Visualizar lista \n',
         '2 - Adicionar tarefa \n',
         '3 - Marcar tarefa como concluída\n',
         '4 - Excluir tarefa\n',
         '5 - Priorizar\n',
         '6 - Sair')
    
    opc = int(input("Opção: "))

    return opc
