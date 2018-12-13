import psutil, time

try:
    arq = open('log.txt', 'a')
    for i in range(10):
        tempo_atual = time.ctime(time.time())
        uso_memoria = '{:6.2f}'.format(psutil.virtual_memory().percent)
        uso_cpu = '{:6.2f}'.format(psutil.cpu_percent())
        texto = tempo_atual + ' '
        texto = texto + uso_memoria + ' '
        texto = texto + uso_cpu + '\n'
        arq.write(texto)
        time.sleep(1)
    arq.close()
except Exception as erro:
    print(str(erro))
