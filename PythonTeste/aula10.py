# If else
nome = str(input("Qual seu nome? "))
if nome == "Fernando":
    print("Que nome bonito!")
else:
    print("Seu nome é tão simples!")
print(f"Bom dia, {nome}")
#-------------------------------------------------------
n1 = float(input("Qual a primeira nota? "))
n2 = float(input("Qual a segunda nota? "))
m = (n1 + n2)/2
print(f"A sua média foi {m:.2f}")
if m >=6.0:
    print("Sua média foi boa, você está aprovado!")
else:
    print("Sua média foi baixa, você está reprovado!")
