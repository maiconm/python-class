file = open('arq1.txt')
linhas = file.readlines()
file.close()

nova_linha = ''

for linha in linhas:
    nova_linha += linha.replace('\n', ' OR ')

file = open('arq2.txt', 'w')
file.write(nova_linha)
file.close()

file = open('arq2.txt')
linhas = file.readlines()
file.close()
print(linhas[0])
