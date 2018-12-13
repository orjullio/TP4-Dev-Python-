#o comando time.time() obtém o tempo em segundos. O comando time.ctime() converte para o tempo local.
import time, psutil

tempo_atual = time.ctime(time.time())

#obtendo o percentual do uso de memória.


for i in range(10):
    tempo_atual = time.ctime(time.time())
    uso_memoria = psutil.virtual_memory().percent
    uso_cpu = psutil.cpu_percent()
    print(tempo_atual, uso_memoria)
    time.sleep(1)