a=float(input('введите число: '))
if a>=0:
    if a==0:
        for i in range(1000):
            print('ОШИБКА СТОП 00000000')
    else:
        print('положительное')
else:
    print('отрицательное')
