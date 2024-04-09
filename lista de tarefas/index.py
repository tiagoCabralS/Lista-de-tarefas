from funcoes import *
from time import sleep

tasks = []

print('-' * 42)
print(f'{"LISTA DE TAREFAS":^42}')
print('-' * 42)

while True:
    opc = funcoes()
    print('-' * 42)

    if opc == 6:
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
        ind = int(input("Tarefa a ser excluída: "))
        excluir(tasks, ind)
        sleep(1)

    elif opc == 5:
        priorizar(tasks)
        sleep(1)
    
    print('-' * 42)
