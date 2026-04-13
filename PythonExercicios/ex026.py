frase = str(input("Digite uma frase: ")).upper().strip()
vezes = frase.count('A')
primeira = frase.find('A')+1
ultima = frase.rfind('A')+1
print(f"A Letra A aparece {vezes} na frase. ")
print(f"A primeira letra A aparece na posição {primeira}")
print(f"A última letra A aparece na posição {ultima}")

