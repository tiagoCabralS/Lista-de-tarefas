def add(lista):
    quant = int(input("Quantas tarefas deseja adicionar? "))

    for c in range(0, quant):
        tarefa = input(f'{c+1}° Tarefa: ')
        lista.append([tarefa, False])

    print(f'\033[0;32;40mTarefas adicionadas!\033[m')

def visualizar(lista):
    for c in range(0, len(lista)):
        print(f"[{'x' if lista[c][1] == True else ' '}] {c} - {lista[c][0]}")

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

def funcoes():
    print(' 1 - Visualizar lista \n',
         '2 - Adicionar tarefa \n',
         '3 - Marcar tarefa como concluída\n',
         '4 - Excluir tarefa\n',
         '5 - Sair')
    
    opc = int(input("Opção: "))

    return opc