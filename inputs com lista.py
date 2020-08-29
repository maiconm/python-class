# Exercicio 3 - inserir 5 nomes e listar em ordem alfabetica
nome1 = input('digite o primeiro nome: ')
nome2 = input('digite o segundo nome: ')
nome3 = input('digite o terceiro nome: ')
nome4 = input('digite o quarto nome: ')
nome5 = input('digite o quinto nome: ')

listaDeNomes = [nome1, nome2, nome3, nome4, nome5]

listaDeNomes.sort()

print(listaDeNomes)
