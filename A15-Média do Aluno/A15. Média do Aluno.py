n1 = float(input("1ª nota: "))
n2 = float(input("2ª nota: "))
n3 = float(input("3ª nota: "))
n4 = float(input("4ª nota: "))

m = (n1 + n2 + n3 + n4) / 4

if m >= 5:
    print("Aprovado!")
else:
    print("Reprovado!")

print("Média:", m)
