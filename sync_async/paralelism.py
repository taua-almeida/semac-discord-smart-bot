# Paralelismo
import multiprocessing
import time


def tarefa():
    print(f"Iniciando tarefa no processo {multiprocessing.current_process().name}")
    time.sleep(2)
    print(f"Tarefa concluída no processo {multiprocessing.current_process().name}")


# Criando dois processos
process1 = multiprocessing.Process(target=tarefa, name="Processo-1")
process2 = multiprocessing.Process(target=tarefa, name="Processo-2")

# Iniciando os processos
process1.start()
process2.start()

# Aguardando a conclusão dos processos
process1.join()
process2.join()

print("Todos os processos concluídos")
