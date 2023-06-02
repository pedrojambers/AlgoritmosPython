if __name__ == '__main__':
    i = 0
    valorLista = []
    while(i <= 2):
        valor = input("Informe um valor inteiro:\n")
        if valor.isdigit():
            valorLista.append(int(valor))
        else:
            print("O valor informado não foi um inteiro!")

        if i == 2:
            valor0 = valorLista[0] * valorLista[0]
            valor1 = valorLista[1] * valorLista[1]
            valor2 = valorLista[2] * valorLista[2]
            print(valor0 + valor1 + valor2)

        i = i + 1