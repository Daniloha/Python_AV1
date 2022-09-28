Nota_1 = float(input("Digite a primeira nota: "))
Nota_2 = float(input("Digite a segunda nota: "))
Nota_3 = float(input("Digite a terceira nota: "))

Media = (Nota_1 + Nota_2 + Nota_3)/3

if Media >= 6:
    print(f"Sua média é {Media:.2f}, você está aprovado!")
elif (Media < 6) and (Media >= 4):
    print(f"Sua média é {Media:.2f}, você está em recuperação!")
else:
    print(f"Sua média é {Media:.2f}, você está reprovado!")