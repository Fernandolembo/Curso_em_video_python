valor = int(input("Qual o valor da casa: R$"))
salario = int(input("Qual seu salário: R$"))
ano = int(input("E quantos anos você vai pagar? "))
prestacao = valor / (ano * 12)
print(f"Para pagar uma casa de R$ {valor} em {ano}, a prestação será de R$ {prestacao:.2f}")
if prestacao <= 30 * 0.30:
    print("Empréstimo CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")