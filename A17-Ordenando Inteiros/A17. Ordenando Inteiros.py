array = []
for i in range(12):
    elemento = int(input("Digite um número inteiro: "))
    array.append(elemento)

array.sort(reverse=True)

print("Ordem decrescente:")
for elemento in array:
    print(elemento)
