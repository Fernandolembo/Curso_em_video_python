velocidade = float(input("Qual a velocidade atual do carro? "))
if velocidade > 50:
    print("MULTADO! Você excedeu o limite permitido que é de 50Km/h")
    multa = (velocidade-50) * 7
    print(f"Você deve pagar uma multa no valor de R$ {multa:.2f}")
print("Tenha um bom dia. Dirija com segurança!")



