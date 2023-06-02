def validaNome(pNome):
    if pNome == "":
        fraseRetorno = "Um para você, um para mim."
    else :
        fraseRetorno = f"Um para {pNome} um para mim"
    return fraseRetorno

if __name__ == '__main__':
    print("Seja Bem-Vindo ao Two-Fer")
    vNome = input("Informe um nome: ")
    print(validaNome(vNome))