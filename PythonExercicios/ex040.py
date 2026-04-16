nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1} e {nota2} a média do aluno é {media}")
if media >= 6:
    print('O aluno está APROVADO')
elif 5 <= media < 6:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está REPROVADO')