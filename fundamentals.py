# lista
salada = ['Abacaixi', 123, True]
print(salada)


# lista vazia
frutas = []

# adiciona item a lista
frutas.append('uva')
frutas.append('laranga')
frutas.append('banana')
frutas.append('pera')
print(frutas)

# remove ultimo item
frutas.pop()

# remove item expecifico
frutas.remove('uva')

# concatenacao de strings

nome = 'camila'
sobrenome = 'pitanga'
nome_e_sobrenome = nome + ' ' + sobrenome
print(nome_e_sobrenome)


altura = 1.78

nome_e_altura = nome + ' tem ' + str(altura) + ' de altura'
print(nome_e_altura)

# usar str() para converter variaveis para string

nome = 'Maicon'
quantidade_letras = len(nome)
print(quantidade_letras)

# usar () quando mostrar mais de uma variavel no print()
print('%s tem %d letras' % (nome, quantidade_letras))

nome = 'maicon'
primeira_letra = nome[0]
ultima_letra = nome[5]

print('primeira letra %s e ultima letra %s' % (primeira_letra, ultima_letra))

# ultima letra de qualquer nome
nome = 'maiconzzzz'
ultima_letra = nome[len(nome) - 1]
print(ultima_letra)

# parse string
primeira_silaba = nome[0:2]
print(primeira_silaba)

# ou (se for 0 o 1o parametro)
primeira_silaba = nome[:2]
print(primeira_silaba)

# funcoes de string
nome = 'Maicon'
print(nome)
nome = nome.lower()
print(nome)
nome.upper()
print(nome)

# substituicao
nome = 'Maicon'
nome = nome.replace('n', 'm')
print(nome)

# trim do js
nome = 'Maicon        '
print('*%s*' % nome)
nome = nome.strip()
print('*%s*' % nome)

# busca
nome = 'Camila'
res = nome.startswith('Cami')
print(res)
res = nome.endswith('la')
print(res)

frase = 'hoje o dia esta com sol'
res = frase.find('sol')
print(res)
frase = 'chuvoso'
res = frase.find('sol')
# -1 quando nao achar a posicao
print(res)

# separar string
dados = 'nome; cpf; idade; endereco'
dados_separados = dados.split(';')
print(dados_separados)

# condicionais
if True:
    print('Verdadeiro')

# Condicionais basicas
# <, <=, >, >=, ==, !=
x = 7
y = 1

if x > y:
    print('x eh maior que y')

print(1 == 1)
print(9 < 2)
print(3 >= 3)
print(3 > 3)
print(12 != 2)
print([1, 2] == [1, 3])

print(2 == 2 and 2 > 1)
print(2 == 2 and 2 > 3)
print(9 <= 10 or 5 == 7)
print(8 == 10 and 5 == 7)

print(not (1 == 1))

# if e else
k = 20
w = 20

if k > w:
    print('k > w')
elif k < w:
    print('k < w')
else:
    print('nao eh maior nem menor.')

# for

times = ['Parana', 'Coritiba', 'Atletico']

for time in times:
    print('%s eh um time de Curitiba' % (time))


