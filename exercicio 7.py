vezes_chamada = 0

def conta_consoantes(string):
    global vezes_chamada
    total_consoantes = 0
    for letra in string.lower():
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
            total_consoantes += 1

    vezes_chamada += 1
    return total_consoantes


string = 'maicon'
print('%s tem %d consoantes' % (string, conta_consoantes(string)))
print('%s tem %d consoantes' % (string, conta_consoantes(string)))
print('funcao chamada %d vezes' % vezes_chamada)
