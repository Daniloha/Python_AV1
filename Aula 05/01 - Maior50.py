Numero = 0
while Numero < 50:
    Numero = float(input("Digite um numero: "))
    if Numero > 50:
        print(f"A metade de {Numero} é {Numero/2 :.2f}")
    else:
        print("O numero é menor que 50")