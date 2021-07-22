lista = [5,7,2,9,4,1,3]
soma = sum(lista)
tamanho = len(lista)
lista.sort()

max = 0
min = 0
for c in range (0, 7):
    if c == 0:
        max = min = lista[c]
    else:
        if lista[c] > max:
            max = lista[c]
        if lista[c] < min:
            min = lista[c]
print('=-' *30)
print(f'tanho da lista: {tamanho}')
print(f'O maior valor digitado foi {max}')
print(f'O menor valor digitado foi {min}')
print(f'A soma dos valores desta lista é: {soma}')
print(f'lista em ordem crescente: {lista}')
