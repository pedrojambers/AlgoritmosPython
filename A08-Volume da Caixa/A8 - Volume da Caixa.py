def calculaVolume(pComprimento, pLargura, pAltura):
    volume = pComprimento * pLargura * pAltura
    return float(volume)

if __name__ == '__main__':
    print("Seja bem vindo!")
    vComprimento = float(input("Informe o comprimento da caixa:\n"))
    vLargura = float(input("Informe a largura da caixa:\n"))
    vAltura = float(input("Informe a altura da caixa:\n"))

    print(calculaVolume(vComprimento, vLargura, vAltura))