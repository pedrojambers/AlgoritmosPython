if __name__ == '__main__':
    salarioMensal = int(input("Informe seu salário:\n"))


    numeroReajuste = int(input("Infome a porcentagem a ser descontada do salário:\n"))


    qtDescontada = salarioMensal * (numeroReajuste / 100)

    salarioFinal = salarioMensal - qtDescontada

    print(salarioFinal)