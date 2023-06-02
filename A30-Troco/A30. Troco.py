valorTotal = float(input("Valor total a ser pago: "))
valorPago = float(input("Valor efetivamente pago: "))

troco = valorPago - valorTotal

if troco < 0:
    print("Valor insuficiente.")
else:
    cedulas = [100, 50, 10, 5, 1]
    moedas = [0.50, 0.10, 0.05, 0.01]
    qtdCedulas = [0, 0, 0, 0, 0]
    qtdMoedas = [0, 0, 0, 0]

    for i in range(len(cedulas)):
        qtdCedulas[i] = int(troco // cedulas[i])
        troco = troco % cedulas[i]

    for i in range(len(moedas)):
        qtdMoedas[i] = int(troco // moedas[i])
        troco = round(troco % moedas[i], 2)

    print("Troco: ")
    for i in range(len(cedulas)):
        if qtdCedulas[i] > 0:
            print(f"{qtdCedulas[i]} cédula(s) de R${cedulas[i]}")

    for i in range(len(moedas)):
        if qtdMoedas[i] > 0:
            print(f"{qtdMoedas[i]} moeda(s) de R${moedas[i]}")
