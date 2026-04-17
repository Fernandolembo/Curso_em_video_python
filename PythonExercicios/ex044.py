preco = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista no dinheiro 
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    desconto = preco - (preco * 0.10)
    print(f"Sua compra de R${preco:.2f} vai custar R${desconto:.2f} no final ")
elif opcao == 2:
    desconto = preco - (preco * 0.05)
    print(f"Sua compra de R${preco:.2f} vai custar R${desconto:.2f} no final ")
elif opcao == 3:
    parcela = preco / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} sem juros")
elif opcao == 4:
    qtd = (int(input("Em quantas parcelas?")))
    juros = (preco * 0.20)
    parcela = (preco / qtd) + juros / qtd
    valor_final = preco + juros
    print(f"Sua compra será parcelada em {qtd}x de R${parcela:.2f} COM JUROS")
    print(f"Sua compra de R${preco:.2f} vai custar R${valor_final:.2f}")
else:
    opcao = 0
    print('Opção inválida de pagamento. Tente novamente.')


