inicio = int(input("Número inicial do intervalo: "))
fim = int(input("Número final do intervalo: "))

quantidadeNumeros = fim - inicio + 1

if quantidadeNumeros != 100:
    print("O intervalo informado não contém 100 números.")
else:
    soma = sum(range(inicio, fim + 1))
    print("Soma dos valores no intervalo:", soma)
