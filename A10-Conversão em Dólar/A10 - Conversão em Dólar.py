if __name__ == '__main__':
    print("Seja bem vindo")
    qtReais = float(input("Informe a quantidade de reais disponivel:\n"))
    vlCotacao = float(input("Informe o valor da cotação:\n"))

    qtDolar = qtReais / vlCotacao
    print(qtDolar)