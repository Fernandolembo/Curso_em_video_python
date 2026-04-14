dist = int(input("Qual a distância da sua viagem? "))
print(f"Você está prestes a começar sua viagem de {dist} Km.")
if dist <= 200:
    preco = dist * 0.50
    print(f"E o preço da sua passagem será de R$ {preco:2.f}.")
else:
    preco= dist * 0.45
    print(f"E o preço da sua passagem será de R$ {preco:2.f}")
