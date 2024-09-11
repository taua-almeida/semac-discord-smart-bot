# Concorrencia
import threading
import time


def tarefa():
    print(f"Thread {threading.current_thread().name} iniciada")
    time.sleep(2)
    print(f"Thread {threading.current_thread().name} concluída")


# Criando threads
thread1 = threading.Thread(target=tarefa, name="A")
thread2 = threading.Thread(target=tarefa, name="B")

# Iniciando threads
thread1.start()
thread2.start()

# Aguardando conclusão
thread1.join()
thread2.join()

print("Todas as threads concluídas")
