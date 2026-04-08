dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
dias_alugados = dias * 60
km_rodados = km *0.15
total = dias_alugados + km_rodados
print(f"O total a pagar é de R${total:.2f}")