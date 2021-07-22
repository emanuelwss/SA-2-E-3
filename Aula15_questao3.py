lista = []
soma = sum(lista)


max = 0
min = 0
for c in range (0, 20):
    lista.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        max = min = lista[c]
    else:
        if lista[c] > max:
            max = lista[c]
        if lista[c] < min:
            min = lista[c]
        soma = sum(lista)
        media = soma / len(lista)
print('=-' *30)
print(f'O maior valor digitado foi {max}')
print(f'O menor valor digitado foi {min}')
print(f'Media dos valores: {media}')