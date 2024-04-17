def add(dicionario, prioridade=30):
    quant = int(input("Quantas tarefas deseja adicionar? "))
    for c in range(0, quant):
        tarefa = input(f'{c+1}° Tarefa: ')
        # [tarefa, False, prioridade]
        dicionario[c] = {'tarefa':tarefa, 'situacao':False, 'prioridade':prioridade}

def visualizar(dicionario):
    for c in range(0, len(dicionario)):
        print(f"\033[0;{dicionario[c]['prioridade']};40m[{'x' if dicionario[c]['situacao'] == True else ' '}] {c} - {dicionario[c]['tarefa']}\033[m")
        
def concluir(dicionario):
    visualizar(dicionario)

    quant = int(input('Quantas tarefas deseja marcar como concluídas? '))

    for c in range(0, quant):
        tarefa = int(input(f'{c+1}° Tarefa: '))
        dicionario[c]['situacao'] = True

def excluir(dicionario):
    visualizar(dicionario)
    indice = int(input("Tarefa a ser excluída: "))
    del(dicionario[indice])

dic = {}
add(dic)
print(dic)
concluir(dic)
excluir(dic)
print(dic)
visualizar(dic)
