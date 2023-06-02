inicio = int(input("Número inicial do intervalo: "))
fim = int(input("Número final do intervalo: "))

soma = 0

for num in range(inicio, fim + 1):
    if num % 2 == 0:
        soma += num

print("A soma dos números pares no intervalo é:", soma)