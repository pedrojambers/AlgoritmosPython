entrada = input("Digite uma palavra, frase ou número: ")

entrada = entrada.replace(" ", "").lower()

if entrada == entrada[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
