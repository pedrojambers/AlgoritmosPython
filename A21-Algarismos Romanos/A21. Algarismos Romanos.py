romano = input("Digite um numeral romano: ")

valores = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

total = 0
anterior = 0

for letra in romano[::-1]:
    valor = valores[letra]

    if valor >= anterior:
        total += valor
    else:
        total -= valor

    anterior = valor

print("O numeral romano", romano, "corresponde ao número", total)
