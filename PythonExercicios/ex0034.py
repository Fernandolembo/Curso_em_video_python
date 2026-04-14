salario = float(input("QUal o salário do funcionário? "))
if salario <= 3000:
    salario = salario * 1.15
else:
    salario = salario * 1.10
print(f"O novo valor do salário é R$ {salario:.2f}")