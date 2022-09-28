from asyncio.windows_events import NULL
Ano = NULL
while Ano != 2022:
    Ano = int(input("Ano atual: "))
    if Ano != 2022:
        print("Error!")
    
Nascimento = int(input("Ano de nascimento: "))
print(f"Sua idade é: {Ano - Nascimento}")

if (Ano - Nascimento) >= 21:
    print("E você já está na maioridade!")
else:
    print("Você não atingiu a maioridade!")