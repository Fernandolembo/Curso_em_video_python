# Definimos a "situação" do caminho para o computador saber o que responder
# caminho = input('Onde tem caminho? (esquerda/direita/frente): ').lower()

# if caminho == 'esquerda':
   # print('O carro segue pela esquerda.')
   # print('Faz manobra: direita, segue, direita, esquerda, segue, direita, segue.')
# elif caminho == 'direita':
    # print('O carro segue pela direita.')
   # print('Faz manobra: esquerda, segue, esquerda, segue.')
# else:
   # print('O carro segue em frente.')
   # print('Carro parou.')

nome = str(input("Qual o seu nome? "))
if nome == 'Fernando':
    print(f"Que nome bonito, {nome}!")
elif nome == 'Luiza' or nome =='Eliana' or nome == 'Letícia':
    print("Seu nome é bem bonito também")
elif nome in 'Ana' or nome == 'Cláudia' or nome == 'Juliana':
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal...")
print(f"Tenha um bom dia, {nome}! ")