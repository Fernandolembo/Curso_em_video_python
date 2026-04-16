seg1 = seg_1 = int(input("Primeiro segmento: "))
seg2 = int(input("Segundo segmento: "))
seg3 = int(input("Terceiro segmento: "))
if seg1 == seg2 == seg3:
    print("O segmento acima pode formar um triângulo EQUILÁTERO")
elif seg1 != seg2 != seg3 != seg1:
    print("O segmento acima pode formar um triângulo ESCALENO")
else:
    print("O segmento acima pode formar um triângulo ISÓCELES")