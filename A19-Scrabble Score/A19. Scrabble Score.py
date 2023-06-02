tabela = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}

palavra = input("Digite uma palavra: ").upper()
score = 0

for letra in palavra:
    for letras, valor in tabela.items():
        if letra in letras:
            score += valor
            break

print("Score da palavra:", score)
