nome_arquivo = input('Entre com o nome do arquivo: ')
num_palavras = 0
try:
    arq = open(nome_arquivo, 'r')
    for linha in arq:
        palavras = linha.split()
        num_palavras += len(palavras)
        arq.close()
except Exception as erro:
    print(str(erro))