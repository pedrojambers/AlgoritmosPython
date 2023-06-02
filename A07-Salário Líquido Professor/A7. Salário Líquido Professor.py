horasTrabalhadas = int(input("Numero de horas trabalhadas no mes: "))
valorHora = float(input("Valor hora-aula: "))
inss = float(input("Percentual de desconto do INSS: "))

salarioBruto = horasTrabalhadas * valorHora
desconto = salarioBruto * (inss / 100)
salarioLiquido = salarioBruto - desconto

print("Salário bruto: R$", salarioBruto)
print("Salário líquido: R$", salarioLiquido)