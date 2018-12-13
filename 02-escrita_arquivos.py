#é importante o arquivo existir, pois ele será apagado se for aberto no modo escrita.

arq = open('arquivo_texto.txt', 'w')
arq.write('Ah moleque!\n')
arq.write('linha dois\n')
arq.write('linha tres\n')
arq.close()

