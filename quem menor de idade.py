n1 = input('nome 1: ')
i1 = input('idade 1: ')
n2 = input('nome 2: ')
i2 = input('idade 2: ')
n3 = input('nome 3: ')
i3 = input('idade 3: ')

menores_de_idade = []

if int(i1) < 18:
    menores_de_idade.append(n1)
if int(i2) < 18:
    menores_de_idade.append(n2)
if int(i3) < 18:
    menores_de_idade.append(n3)

print(menores_de_idade)
