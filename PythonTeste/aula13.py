# Repetição for

for c in range(0,6):
    print('Oi')
print('FIM')

#Contagem de números
for c in range(1,7):
    print(c)

# De trás pra frente
for c in range(6,0, -1):
    print(c)

# Pulando de 2 em 2
for c in range(0,7,2):
    print(c)

n = int(input("Digite um número"))
for c in range (0,n):
    print(c)

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print('FIM')

# Ler valores varias vezes
for c in range(0,10):
    n = int(input("Digite um valor: "))
print('fim')

# Somando valores
s = 0
for c in range(0,10):
    n = int(input("Digite um valor: "))
    s += n
print(f"O somatório de todos os valores foi {s}")