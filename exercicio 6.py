max = 100
i = 50

while i <= max:
    if (i % 2) == 0:
        i += 1
        continue
    print('%d eh um numero impar' % i)
    i += 1
