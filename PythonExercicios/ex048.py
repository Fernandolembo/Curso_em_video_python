s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 ==0:
        cont = cont + 1
        s = s + c
print(f"O somatório de todos os {cont} valores solicitados é {s}")