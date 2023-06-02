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
            print(valorLista[0] + valorLista[1] + valorLista[2])

        i = i + 1


