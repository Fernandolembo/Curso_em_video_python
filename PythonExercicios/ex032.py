import datetime
import calendar
ano_atual = datetime.date.today().year
ano = int(input("Qual ano quer analisar? Digite 0 para o ano atual: "))
if ano == 0:
    ano = ano_atual
if calendar.isleap(ano):
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO é bissexto.")

