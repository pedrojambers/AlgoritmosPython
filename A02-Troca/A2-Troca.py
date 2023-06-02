if __name__ == '__main__':
    A = input("Informe valores para A!\n")
    B = input("Informe valores para B!\n")

    C = A
    D = B

    A = D
    B = C

    print(f"O novo valor de A é {A}\nO novo valor de B é {B}")