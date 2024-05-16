print('Operação de Divisão')
while True:
    n1=int(input('Informe o primeiro número: '))
    n2=int(input('Informe o segundo número: '))
    if n2 == 0:
        print('Divisor não pode ser 0')
        break
    print(f"{n1} / {n2} = {n1/n2}")
    print(f"{20 * 'x'}")
print('Fim do programa')