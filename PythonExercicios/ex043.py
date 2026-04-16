peso = float(input("Qual seu peso? (Kg) "))
altura = float(input("Qual sua altura? (m) "))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.2f}")
if imc <= 18.5:
    print("Você está ABAIXO do peso normal")
elif 18.5 <= imc < 25:
    print("Você está no peso IDEAL")
elif 25 <= imc < 30:
    print("Você está com SOBREPESO")
elif 30 <= imc < 40:
    print("Você está com OBESIDADE")
else:
    print("Você esta em OBESIDADE MÓRBIDA")