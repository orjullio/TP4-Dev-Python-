# Obtendo informações através do processo psutil
import psutil
import time
import os
import time  # para o sleep

def comparacao(l):
    return(l['cpu_percent'])

for i in range(10):
    lista = []
    for proc in psutil.process_iter():
        try:
            for proc in psutil.process_iter():
                pinfo = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
                print(pinfo)
                time.sleep(1)
        except psutil.NoSuchProcess:
            pass

        os.system('cls')
        if lista:
            titulo = '{:<6}'.format("PID")
            titulo = titulo + '{:<20.19}'.format("Nome")
            titulo = titulo + '{:>6}'.format("%CPU")
            print(titulo)
            lista_ordenada = sorted(lista, key=comparacao, reverse=True)
            for i in lista_ordenada[0:15]:
                texto = '{:<6}'.format(i['pid'])
                texto = texto + '{:<20.19}'.format(i['name'])
                texto = texto + '{:>6}'.format(i['cpu_percent'])

