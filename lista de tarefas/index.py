from funcoes import *
from time import sleep

tasks = {'tarefa':[], 'situacao':[], 'prioridade':[]}

print('-' * 42)
print(f'{"LISTA DE TAREFAS":^42}')
print('-' * 42)

while True:
    opc = funcoes()

    if opc == 7:
        print('Saindo..')
        sleep(1)
        break

    elif opc == 1:
        visualizar(tasks)
        sleep(1)

    elif opc == 2:
        add(tasks)
        sleep(1)
    
    elif opc == 3:
        concluir(tasks)
        sleep(1)
    
    elif opc == 4:
        excluir(tasks)
        sleep(1)

    elif opc == 5:
        priorizar(tasks)
        sleep(1)

    elif opc == 6:
        editar(tasks)
        sleep(1)
