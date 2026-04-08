preco = float(input("Qual é o preço do produto? R$ "))
valor = preco - (preco * 5 / 100)
print(f"O produto que custava {preco:.2f}, na promoção com desconto de 5% vai custar R${valor:.2f}")