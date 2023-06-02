votosValidosA = int(input("Quantidade de votos válidos para o candidato A: "))
votosValidosB = int(input("Quantidade de votos válidos para o candidato B: "))
votosValidosC = int(input("Quantidade de votos válidos para o candidato C: "))
votosNulos = int(input("Quantidade de votos nulos: "))
votosEmBranco = int(input("Quantidade de votos em branco: "))

totalEleitores = votosValidosA + votosValidosB + votosValidosC + votosNulos + votosEmBranco

percentualValidos = (votosValidosA + votosValidosB + votosValidosC) / totalEleitores * 100
percentualVotosValidosA = votosValidosA / totalEleitores * 100
percentualvotosValidosB = votosValidosB / totalEleitores * 100
percentualvotosValidosC = votosValidosC / totalEleitores * 100
percentualvotosNulos = votosNulos / totalEleitores * 100
percentualvotosEmBranco = votosEmBranco / totalEleitores * 100

print("Número total de eleitores:", totalEleitores)
print("Percentual de votos válidos em relação à quantidade de eleitores:", percentualValidos, "%")
print("Percentual de votos válidos para o candidato A em relação à quantidade de eleitores:", percentualVotosValidosA, "%")
print("Percentual de votos válidos para o candidato B em relação à quantidade de eleitores:", percentualvotosValidosB, "%")
print("Percentual de votos válidos para o candidato C em relação à quantidade de eleitores:", percentualvotosValidosC, "%")
print("Percentual de votos nulos em relação à quantidade de eleitores:", percentualvotosNulos, "%")
print("Percentual de votos em branco em relação à quantidade de eleitores:", percentualvotosEmBranco, "%")
