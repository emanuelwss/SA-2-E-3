vp = int(input('valor a pagar: '))
vr = int(input('valor recebido: '))
troco = vr - vp
print('=' * 30)
print(f'valor de troco é: {troco}')
ced = 50
totced = 0
while True:
    if troco >= ced:
        troco -= ced
        totced += 1
    else:
        print(f'{totced} nota: R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if troco == 0:
            break
