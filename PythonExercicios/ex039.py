from datetime import date
ano = int(input("Ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - ano
print(f"Quem nasceu em {ano} tem {idade} em {anoAtual}")
if idade <= 17:
    alistamento = 18 - idade
    futuro = anoAtual + alistamento
    print(f"Ainda faltam {alistamento} anos para o alistamento.")
    print(f"Seu alistamento será em {futuro}.")
elif idade >= 19:
    alistamento = idade - 18
    passado = anoAtual - alistamento
    print(f"Você ja deveria estar alistado há {alistamento} anos.")
    print(f"Seu alistamento foi em {passado}.")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE")
