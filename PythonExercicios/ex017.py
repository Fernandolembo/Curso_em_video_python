from math import hypot
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjascente = float(input("Comprimento do cateto adjascente: "))
print(f"A hipotenusa vai medir {hypot(cateto_oposto, cateto_adjascente):.2f}")
