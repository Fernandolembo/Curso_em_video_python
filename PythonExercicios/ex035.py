seg_1 = int(input("Primeiro segmento: "))
seg_2 = int(input("Segundo segmento: "))
seg_3 = int(input("Terceiro segmento:"))
if seg_1+ seg_2 > seg_3 and seg_2+ seg_3 > seg_1 and seg_3 + seg_1 > seg_2:
    print("Os segmentos acima PODEM formar um triângulo")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo")