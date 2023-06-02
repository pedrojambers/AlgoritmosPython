if __name__ == '__main__':
    print("Seja bem vindo!")
    distancia = float(input("Informe a distancia:\n"))
    tempo = int(input("Informe o tempo:\n"))

    velocidade = (distancia * 1000) / (tempo * 60)
    print(velocidade)